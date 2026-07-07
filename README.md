# Macrolitter video counting on riverbanks using state space models and moving cameras
Mathis Chagneux, Sylvain Le Corff, Pierre Gloaguen, Charles
Ollion, Océane Lepâtre, Antoine Bruge
2023-02-16

### Citation

Mathis Chagneux, Sylvain Le Corff, Pierre Gloaguen, Charles Ollion, Océane Lepâtre and Antoine Bruge (February 2023). Macrolitter video counting on riverbanks using state space models and moving cameras. Computo.
<https://doi.org/10.57750/845m-f805>

### Badges

[![build and
publish](https://github.com/computorg/published-202301-chagneux-macrolitter/actions/workflows/build.yml/badge.svg)](https://github.com/computorg/published-202301-chagneux-macrolitter/actions/workflows/build.yml)
[![reviews](https://img.shields.io/badge/review-report-blue)](https://github.com/computorg/published-202301-chagneux-macrolitter/issues?q=is%3Aopen+is%3Aissue+label%3Areview)
[![SWH](https://archive.softwareheritage.org/badge/origin/https://github.com/computorg/published-202301-chagneux-macrolitter)](https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/computorg/published-202301-chagneux-macrolitter)
[![DOI:10.57750/845m-f805](https://img.shields.io/badge/DOI-10.57750%2F845m--f805-034E79.svg)](https://doi.org/10.57750/845m-f805)
[![Creative Commons
License](https://i.creativecommons.org/l/by/4.0/80x15.png)](http://creativecommons.org/licenses/by/4.0/)

### Authors’ affiliations

- [Mathis Chagneux](https://www.linkedin.com/in/mathis-chagneux-140245158/?originalSubdomain=fr) (Telecom Paris, LTCI)
- [Sylvain Le Corff](https://sylvainlc.github.io/) (Sorbonne Université, UMR 8001 (LPSM))
- [Pierre Gloaguen](https://papayoun.github.io/) (AgroParisTech, UMR MIA 518)
- [Charles Ollion](https://charlesollion.github.io/) (Naia Science)
- [Océane Lepâtre](https://fr.linkedin.com/in/oc%C3%A9ane-lep%C3%A2tre-675b38116) (Surfrider Foundation Europe)
- [Antoine Bruge](https://www.linkedin.com/in/antoinebruge/) (Surfrider Foundation Europe)

### Abstract

Litter is a known cause of degradation in marine environments and most
of it travels in rivers before reaching the oceans. In this paper, we
present a novel algorithm to assist waste monitoring along watercourses.
While several attempts have been made to quantify litter using neural
object detection in photographs of floating items, we tackle the more
challenging task of counting directly in videos using boat-embedded
cameras. We rely on multi-object tracking (MOT) but focus on the key
pitfalls of false and redundant counts which arise in typical scenarios
of poor detection performance. Our system only requires supervision at
the image level and performs Bayesian filtering via a state space model
based on optical flow. We present a new open image dataset gathered
through a crowdsourced campaign and used to train a center-based
anchor-free object detector. Realistic video footage assembled by water
monitoring experts is annotated and provided for evaluation.
Improvements in count quality are demonstrated against systems built
from state-of-the-art multi-object trackers sharing the same detection
capabilities. A precise error decomposition allows clear analysis and
highlights the remaining challenges.
