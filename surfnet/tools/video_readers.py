import cv2

class FramesWithInfo:
    def __init__(self, frames, output_shape=None):
        self.frames = frames
        if output_shape is None: 
            self.output_shape = frames[0].shape[:-1][::-1]
        else: self.output_shape = output_shape
        self.end = len(frames)
        self.read_head = 0
    
    def __next__(self):
        if self.read_head < self.end:
            frame = self.frames[self.read_head]
            self.read_head+=1
            return frame

        else: 
            raise StopIteration
    
    def __iter__(self):
        return self
        
class AdvancedFrameReader():
    def __init__(self, video_name, read_every, rescale_factor, init_time_min, init_time_s):

        self.cap = cv2.VideoCapture(video_name)

        self.original_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.original_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        if rescale_factor != 1:
            self.set_rescale_factor(rescale_factor)
        else: 
            self.original_shape_mode = True

        self.init_rescale_factor = rescale_factor


        self.frame_skip = read_every -  1
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)/read_every
        print('Reading at {} fps.'.format(self.fps))

        self.set_time_position(init_time_min, init_time_s)     
        self.init_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        self.total_num_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)


    def post_process(self, ret, frame):
        if ret: 
            if self.original_shape_mode:
                return ret, frame
            else:
                return ret, cv2.resize(frame, self.new_shape)
        else:
            return ret, [] 

    def skip(self):
        if not self.nb_frames_read:
            return 
        else:
            for _ in range(self.frame_skip):
                self.cap.read()

    def read_frame(self):

        self.skip()
        ret, frame = self.cap.read()
        self.nb_frames_read += 1
        return self.post_process(ret, frame)

    def set_time_position(self, time_min, time_s):
        time = 60 * time_min  + time_s
        self.cap.set(cv2.CAP_PROP_POS_MSEC, 1000 * time)
        self.init_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        print('Reading from {}min{}sec'.format(time_min,time_s))
        self.nb_frames_read = 0

    def reset_init_frame(self):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES,int(self.init_frame))
        self.nb_frames_read = 0 

    def set_init_frame(self, init_frame):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, int(init_frame))
        self.init_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        self.nb_frames_read = 0

    def set_rescale_factor(self, rescale_factor):
        width = int(self.original_width/rescale_factor)
        height = int(self.original_height/rescale_factor)
        self.new_shape  = (width, height)
        self.original_shape_mode = False
        print('Reading in {}x{}'.format(width, height))

    def set_original_shape_mode(self, mode):
        self.original_shape_mode = mode

    def reset_init_rescale_factor(self):
        self.set_rescale_factor(self.init_rescale_factor)

class IterableFrameReader:

    def __init__(self, video_filename, skip_frames=0, output_shape=None):
        self.video = cv2.VideoCapture(video_filename)
        self.input_shape = (self.video.get(cv2.CAP_PROP_FRAME_WIDTH), self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.skip_frames = skip_frames
        if output_shape is None: 
            w, h = self.input_shape
            new_h = (h | 31) + 1
            new_w = (w | 31) + 1
            self.output_shape = (new_w, new_h)
        else:
            self.output_shape = output_shape
        self.fps = self.video.get(cv2.CAP_PROP_FPS) / (self.skip_frames+1)
            
    def __next__(self):
        ret, frame = self.video.read()
        self._skip_frames()
        if ret: 
            return cv2.resize(frame, self.output_shape)
        raise StopIteration

    def __iter__(self):
        return self
    
    def init(self):
        self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    def _skip_frames(self):
        for _ in range(self.skip_frames):
            self.video.read()        

class SimpleVideoReader:
    def __init__(self, video_filename, skip_frames=0):
        self.skip_frames = skip_frames 
        self.video = cv2.VideoCapture(video_filename)
        self.shape = (int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        self.fps = self.video.get(cv2.CAP_PROP_FPS) / (skip_frames+1)
        self.frame_nb = 0
        self.num_frames = self.video.get(cv2.CAP_PROP_FRAME_COUNT)

    def read(self):
        ret, frame = self.video.read()
        self.frame_nb+=1
        self._skip_frames()
        return ret, frame, self.frame_nb-1

    def set_frame(self, frame_nb_to_set):
        self.video.set(cv2.CAP_PROP_POS_FRAMES, frame_nb_to_set)
        self.frame_nb = frame_nb_to_set

    def _skip_frames(self):
        for _ in range(self.skip_frames):
            self.video.read()

