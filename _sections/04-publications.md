---
order: 4
section_id: "publications"
title: "Scientific Papers & Publications"
nav_title: "Publications"
subtitle: "Peer-reviewed conference proceedings and workshop publications in embedded systems, energy-harvesting IoT, and hardware-software co-design."
badge: "Research Output"
badge_icon: "📚"
---

<div style="margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.75rem;">
  <p style="margin: 0; color: var(--text-muted); font-size: 0.95rem;" data-i18n="pub.indexed_in">
    Publications indexed in <strong>IEEE Xplore</strong>, <strong>ACM Digital Library</strong>, and <strong>DBLP</strong>.
  </p>
  <a href="{{ '/assets/papers.bib' | relative_url }}" download class="btn btn-secondary btn-sm" title="Download Complete BibTeX File">
    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
    <span data-i18n="common.download_bib">Download papers.bib</span>
  </a>
</div>

<!-- Paper 1: MCSoC 2025 Best Paper -->
<article class="pub-card">
  <div class="pub-top">
    <span class="pub-venue-badge" style="border-color: #eab308; color: #facc15;">
      🏆 Best Paper Award &bull; IEEE MCSoC 2025
    </span>
    <span class="pub-year">2025</span>
  </div>

  <h3 class="pub-title">
    Early-Exit Neural Architecture Search for Energy-Harvesting Edge Computing
  </h3>

  <div class="pub-authors">
    <span class="author-self">Pierre-Louis Sixdenier</span>, 
    <span>Mark Deutel</span>, 
    <span>Jürgen Teich</span>
  </div>

  <div class="pub-abstract" data-i18n="pub.p1.abstract">
    <strong>Abstract:</strong> Investigates early-exit deep neural network (EE-NN) architecture search tailored for edge computing platforms powered by intermittent energy harvesting, dynamically selecting confidence-based early exits to preserve accuracy under fluctuating ambient power.
  </div>

  <div class="pub-actions">
    <a href="https://doi.org/10.1109/MCSoC67473.2025.00066" class="pub-btn" target="_blank" rel="noopener">
      DOI: 10.1109/MCSoC67473.2025.00066
    </a>
    <a href="https://dblp.org/pid/344/6869.html" class="pub-btn" target="_blank" rel="noopener">DBLP</a>
    <button class="pub-btn" data-toggle-bibtex="bib-sixdenier2025early">BibTeX</button>
  </div>

  <div id="bib-sixdenier2025early" class="bibtex-block">
    <button class="btn btn-secondary btn-sm copy-bibtex-btn" data-copy-target="bib-sixdenier2025early" data-i18n="common.copy">Copy</button>
<code>@inproceedings{sixdenier2025early,
  author    = {Sixdenier, Pierre-Louis and Deutel, Mark and Teich, J{\"u}rgen},
  title     = {Early-Exit Neural Architecture Search for Energy-Harvesting Edge Computing},
  booktitle = {2025 IEEE 18th International Symposium on Embedded Multicore/Many-core Systems-on-Chip (MCSoC)},
  year      = {2025},
  pages     = {372--379},
  doi       = {10.1109/MCSoC67473.2025.00066},
  note      = {Best Paper Award}
}</code>
  </div>
</article>

<!-- Paper 2: ITEM 2026 -->
<article class="pub-card">
  <div class="pub-top">
    <span class="pub-venue-badge">
      ECML-PKDD Workshop &bull; ITEM 2026
    </span>
    <span class="pub-year">September 2026</span>
  </div>

  <h3 class="pub-title">
    Early-Exit Forecasting of Deep Neural Networks on Energy-Harvesting Edge Devices
  </h3>

  <div class="pub-authors">
    <span class="author-self">Pierre-Louis Sixdenier</span>, 
    <span>Mark Deutel</span>, 
    <span>Stefan Wildermann</span>, 
    <span>Jürgen Teich</span>
  </div>

  <div class="pub-abstract" data-i18n="pub.p2.abstract">
    <strong>Abstract:</strong> Proposes early-exit forecasting models allowing energy-harvesting edge sensors to anticipate the computational feasibility of inference branches across future harvesting windows.
  </div>

  <div class="pub-actions">
    <a href="https://item-workshop.org" class="pub-btn" target="_blank" rel="noopener">ITEM 2026</a>
    <a href="https://dblp.org/pid/344/6869.html" class="pub-btn" target="_blank" rel="noopener">DBLP</a>
    <button class="pub-btn" data-toggle-bibtex="bib-sixdenier2026earlyexit">BibTeX</button>
  </div>

  <div id="bib-sixdenier2026earlyexit" class="bibtex-block">
    <button class="btn btn-secondary btn-sm copy-bibtex-btn" data-copy-target="bib-sixdenier2026earlyexit" data-i18n="common.copy">Copy</button>
<code>@inproceedings{sixdenier2026earlyexit,
  author    = {Sixdenier, Pierre-Louis and Deutel, Mark and Wildermann, Stefan and Teich, J{\"u}rgen},
  title     = {Early-Exit Forecasting of Deep Neural Networks on Energy-Harvesting Edge Devices},
  booktitle = {Proceedings of the 7th International Workshop on IoT, Edge, and Mobile for Embedded Machine Learning (ITEM)},
  series    = {Proc. Int. Workshops of ECML-PKDD},
  year      = {2026},
  address   = {Naples, Italy}
}</code>
  </div>
</article>

<!-- Paper 3: EWSN 2025 -->
<article class="pub-card">
  <div class="pub-top">
    <span class="pub-venue-badge">
      EWSN 2025 &bull; Work-in-Progress
    </span>
    <span class="pub-year">2025</span>
  </div>

  <h3 class="pub-title">
    WiP Paper: Utility-Aware Transmission of Sensor Data on Energy-Harvesting IoT Gateways
  </h3>

  <div class="pub-authors">
    <span class="author-self">Pierre-Louis Sixdenier</span>, 
    <span>Jebacyril Arockiaraj</span>, 
    <span>Stefan Wildermann</span>, 
    <span>Jürgen Teich</span>
  </div>

  <div class="pub-abstract" data-i18n="pub.p3.abstract">
    <strong>Abstract:</strong> Introduces utility-aware transmission policies for battery-less or energy-harvesting IoT gateways, dynamically prioritizing high-entropy sensor streams over lossy wireless channels.
  </div>

  <div class="pub-actions">
    <a href="https://dblp.org/rec/conf/ewsn/SixdenierAWT25" class="pub-btn" target="_blank" rel="noopener">DBLP Record</a>
    <button class="pub-btn" data-toggle-bibtex="bib-sixdenier2025ewsn">BibTeX</button>
  </div>

  <div id="bib-sixdenier2025ewsn" class="bibtex-block">
    <button class="btn btn-secondary btn-sm copy-bibtex-btn" data-copy-target="bib-sixdenier2025ewsn" data-i18n="common.copy">Copy</button>
<code>@inproceedings{sixdenier2025ewsn,
  author    = {Sixdenier, Pierre-Louis and Arockiaraj, Jebacyril and Wildermann, Stefan and Teich, J{\"u}rgen},
  title     = {WiP Paper: Utility-Aware Transmission of Sensor Data on Energy-Harvesting IoT Gateways},
  booktitle = {Proceedings of the 22nd International Conference on Embedded Wireless Systems and Networks (EWSN 2025)},
  pages     = {142--147},
  year      = {2025},
  address   = {Leuven, Belgium}
}</code>
  </div>
</article>

<!-- Paper 4: MECO 2024 -->
<article class="pub-card">
  <div class="pub-top">
    <span class="pub-venue-badge">
      IEEE MECO 2024
    </span>
    <span class="pub-year">June 2024</span>
  </div>

  <h3 class="pub-title">
    GRES: Guaranteed Remaining Energy Scheduling of Energy-harvesting Sensors by Quality Adaptation
  </h3>

  <div class="pub-authors">
    <span class="author-self">Pierre-Louis Sixdenier</span>, 
    <span>Stefan Wildermann</span>, 
    <span>Jürgen Teich</span>
  </div>

  <div class="pub-abstract" data-i18n="pub.p4.abstract">
    <strong>Abstract:</strong> Formulates GRES, a scheduling algorithm guaranteeing that embedded sensors maintain a reserved residual energy budget across uncertain solar/kinetic harvesting cycles through continuous task quality adaptation.
  </div>

  <div class="pub-actions">
    <a href="https://doi.org/10.1109/MECO62366.2024.10582998" class="pub-btn" target="_blank" rel="noopener">
      DOI: 10.1109/MECO62366.2024.10582998
    </a>
    <a href="https://dblp.org/rec/conf/meco/SixdenierWT24.html" class="pub-btn" target="_blank" rel="noopener">DBLP</a>
    <button class="pub-btn" data-toggle-bibtex="bib-sixdenier2024gres">BibTeX</button>
  </div>

  <div id="bib-sixdenier2024gres" class="bibtex-block">
    <button class="btn btn-secondary btn-sm copy-bibtex-btn" data-copy-target="bib-sixdenier2024gres" data-i18n="common.copy">Copy</button>
<code>@inproceedings{sixdenier2024gres,
  author    = {Sixdenier, Pierre-Louis and Wildermann, Stefan and Teich, J{\"u}rgen},
  title     = {GRES: Guaranteed Remaining Energy Scheduling of Energy-harvesting Sensors by Quality Adaptation},
  booktitle = {Proceedings of the 13th Mediterranean Conference on Embedded Computing (MECO)},
  year      = {2024},
  pages     = {1--5},
  doi       = {10.1109/MECO62366.2024.10582998},
  publisher = {IEEE}
}</code>
  </div>
</article>

<!-- Paper 5: MEMOCODE 2023 -->
<article class="pub-card">
  <div class="pub-top">
    <span class="pub-venue-badge">
      ACM/IEEE MEMOCODE 2023
    </span>
    <span class="pub-year">September 2023</span>
  </div>

  <h3 class="pub-title">
    Hybrid Genetic Reinforcement Learning for Generating Run-Time Requirement Enforcers
  </h3>

  <div class="pub-authors">
    <span>Jan Spieck</span>, 
    <span class="author-self">Pierre-Louis Sixdenier</span>, 
    <span>Khalil Esper</span>, 
    <span>Stefan Wildermann</span>, 
    <span>Jürgen Teich</span>
  </div>

  <div class="pub-abstract" data-i18n="pub.p5.abstract">
    <strong>Abstract:</strong> Combines evolutionary genetic algorithms with deep reinforcement learning to synthesize verifiable, reactive run-time requirement enforcers for multi-processor systems-on-chip under safety constraints.
  </div>

  <div class="pub-actions">
    <a href="https://doi.org/10.1145/3610579.3611091" class="pub-btn" target="_blank" rel="noopener">
      DOI: 10.1145/3610579.3611091
    </a>
    <a href="https://dblp.org/rec/conf/memocode/SpieckSEWT23.html" class="pub-btn" target="_blank" rel="noopener">DBLP</a>
    <button class="pub-btn" data-toggle-bibtex="bib-spieck2023hybrid">BibTeX</button>
  </div>

  <div id="bib-spieck2023hybrid" class="bibtex-block">
    <button class="btn btn-secondary btn-sm copy-bibtex-btn" data-copy-target="bib-spieck2023hybrid" data-i18n="common.copy">Copy</button>
<code>@inproceedings{spieck2023hybrid,
  author    = {Spieck, Jan and Sixdenier, Pierre-Louis and Esper, Khalil and Wildermann, Stefan and Teich, J{\"u}rgen},
  title     = {Hybrid Genetic Reinforcement Learning for Generating Run-Time Requirement Enforcers},
  booktitle = {Proceedings of the 21st ACM-IEEE International Symposium on Formal Methods and Models for System Design (MEMOCODE '23)},
  year      = {2023},
  pages     = {23--35},
  doi       = {10.1145/3610579.3611091},
  publisher = {ACM}
}</code>
  </div>
</article>

<!-- Paper 6: IEEE EDGE 2023 -->
<article class="pub-card">
  <div class="pub-top">
    <span class="pub-venue-badge">
      IEEE EDGE 2023
    </span>
    <span class="pub-year">July 2023</span>
  </div>

  <h3 class="pub-title">
    Seque: Lean and Energy-aware Data Management for IoT Gateways
  </h3>

  <div class="pub-authors">
    <span class="author-self">Pierre-Louis Sixdenier</span>, 
    <span>Stefan Wildermann</span>, 
    <span>Martin Ottens</span>, 
    <span>Jürgen Teich</span>
  </div>

  <div class="pub-abstract" data-i18n="pub.p6.abstract">
    <strong>Abstract:</strong> Presents Seque, an ultra-lean data storage and compression engine designed for energy-constrained IoT edge gateways, eliminating redundant I/O transactions to maximize battery lifetime.
  </div>

  <div class="pub-actions">
    <a href="https://doi.org/10.1109/EDGE60047.2023.00030" class="pub-btn" target="_blank" rel="noopener">
      DOI: 10.1109/EDGE60047.2023.00030
    </a>
    <a href="https://dblp.org/rec/conf/edge/SixdenierWOT23.html" class="pub-btn" target="_blank" rel="noopener">DBLP</a>
    <button class="pub-btn" data-toggle-bibtex="bib-sixdenier2023seque">BibTeX</button>
  </div>

  <div id="bib-sixdenier2023seque" class="bibtex-block">
    <button class="btn btn-secondary btn-sm copy-bibtex-btn" data-copy-target="bib-sixdenier2023seque" data-i18n="common.copy">Copy</button>
<code>@inproceedings{sixdenier2023seque,
  author    = {Sixdenier, Pierre-Louis and Wildermann, Stefan and Ottens, Martin and Teich, J{\"u}rgen},
  title     = {Seque: Lean and Energy-aware Data Management for IoT Gateways},
  booktitle = {2023 IEEE International Conference on Edge Computing and Communications (EDGE)},
  year      = {2023},
  pages     = {133--139},
  doi       = {10.1109/EDGE60047.2023.00030},
  publisher = {IEEE}
}</code>
  </div>
</article>

<!-- Paper 7: NG-RES 2023 -->
<article class="pub-card">
  <div class="pub-top">
    <span class="pub-venue-badge">
      OASIcs &bull; NG-RES 2023
    </span>
    <span class="pub-year">January 2023</span>
  </div>

  <h3 class="pub-title">
    RAVEN: Reinforcement Learning for Generating Verifiable Run-Time Requirement Enforcers for MPSoCs
  </h3>

  <div class="pub-authors">
    <span>Khalil Esper</span>, 
    <span>Jan Spieck</span>, 
    <span class="author-self">Pierre-Louis Sixdenier</span>, 
    <span>Stefan Wildermann</span>, 
    <span>Jürgen Teich</span>
  </div>

  <div class="pub-abstract" data-i18n="pub.p7.abstract">
    <strong>Abstract:</strong> Develops a reinforcement learning framework that synthesizes formally verifiable run-time enforcers for mixed-criticality multi-processor systems-on-chip.
  </div>

  <div class="pub-actions">
    <a href="https://doi.org/10.4230/OASIcs.NG-RES.2023.7" class="pub-btn" target="_blank" rel="noopener">
      DOI: 10.4230/OASIcs.NG-RES.2023.7
    </a>
    <a href="https://drops.dagstuhl.de/opus/volltexte/2023/17738" class="pub-btn" target="_blank" rel="noopener">OpenAccess</a>
    <button class="pub-btn" data-toggle-bibtex="bib-esper2023raven">BibTeX</button>
  </div>

  <div id="bib-esper2023raven" class="bibtex-block">
    <button class="btn btn-secondary btn-sm copy-bibtex-btn" data-copy-target="bib-esper2023raven" data-i18n="common.copy">Copy</button>
<code>@inproceedings{esper2023raven,
  author    = {Esper, Khalil and Spieck, Jan and Sixdenier, Pierre-Louis and Wildermann, Stefan and Teich, J{\"u}rgen},
  title     = {RAVEN: Reinforcement Learning for Generating Verifiable Run-Time Requirement Enforcers for MPSoCs},
  booktitle = {Fourth Workshop on Next Generation Real-Time Embedded Systems (NG-RES 2023)},
  series    = {OpenAccess Series in Informatics (OASIcs)},
  volume    = {108},
  pages     = {7:1--7:16},
  year      = {2023},
  doi       = {10.4230/OASIcs.NG-RES.2023.7},
  publisher = {Schloss Dagstuhl -- Leibniz-Zentrum f{\"u}r Informatik}
}</code>
  </div>
</article>

<!-- Paper 8: SAMOS 2022 -->
<article class="pub-card">
  <div class="pub-top">
    <span class="pub-venue-badge">
      Springer LNCS &bull; SAMOS XXII
    </span>
    <span class="pub-year">July 2022</span>
  </div>

  <h3 class="pub-title">
    SIDAM: A Design Space Exploration Framework for Multi-sensor Embedded Systems Powered by Energy Harvesting
  </h3>

  <div class="pub-authors">
    <span class="author-self">Pierre-Louis Sixdenier</span>, 
    <span>Stefan Wildermann</span>, 
    <span>Daniel Ziegler</span>, 
    <span>Jürgen Teich</span>
  </div>

  <div class="pub-abstract" data-i18n="pub.p8.abstract">
    <strong>Abstract:</strong> Introduces SIDAM, an automated multi-objective design space exploration tool evaluating heterogeneous sensor configurations and power conditioning circuits for energy-neutral operations.
  </div>

  <div class="pub-actions">
    <a href="https://doi.org/10.1007/978-3-031-15074-6_20" class="pub-btn" target="_blank" rel="noopener">
      DOI: 10.1007/978-3-031-15074-6_20
    </a>
    <a href="https://dblp.org/rec/conf/samos/SixdenierWZT22.html" class="pub-btn" target="_blank" rel="noopener">DBLP</a>
    <button class="pub-btn" data-toggle-bibtex="bib-sixdenier2022sidam">BibTeX</button>
  </div>

  <div id="bib-sixdenier2022sidam" class="bibtex-block">
    <button class="btn btn-secondary btn-sm copy-bibtex-btn" data-copy-target="bib-sixdenier2022sidam" data-i18n="common.copy">Copy</button>
<code>@inproceedings{sixdenier2022sidam,
  author    = {Sixdenier, Pierre-Louis and Wildermann, Stefan and Ziegler, Daniel and Teich, J{\"u}rgen},
  title     = {SIDAM: A Design Space Exploration Framework for Multi-sensor Embedded Systems Powered by Energy Harvesting},
  booktitle = {Embedded Computer Systems: Architectures, Modeling, and Simulation (SAMOS XXII)},
  series    = {Lecture Notes in Computer Science},
  volume    = {13511},
  pages     = {329--345},
  year      = {2022},
  doi       = {10.1007/978-3-031-15074-6_20},
  publisher = {Springer}
}</code>
  </div>
</article>

<!-- Paper 9: ACSOS-C 2021 -->
<article class="pub-card">
  <div class="pub-top">
    <span class="pub-venue-badge">
      IEEE ACSOS-C 2021
    </span>
    <span class="pub-year">September 2021</span>
  </div>

  <h3 class="pub-title">
    Towards an Autonomous, Power-Efficient Base Station for Sensor Data Collection
  </h3>

  <div class="pub-authors">
    <span class="author-self">Pierre-Louis Sixdenier</span>
  </div>

  <div class="pub-abstract" data-i18n="pub.p9.abstract">
    <strong>Abstract:</strong> Examines architectures for self-sustaining solar/ambient-powered IoT base stations, presenting adaptive power management heuristics for uninterrupted sensor ingestion.
  </div>

  <div class="pub-actions">
    <a href="https://doi.org/10.1109/ACSOS-C52956.2021.00083" class="pub-btn" target="_blank" rel="noopener">
      DOI: 10.1109/ACSOS-C52956.2021.00083
    </a>
    <a href="https://dblp.org/rec/conf/acsos/Sixdenier21.html" class="pub-btn" target="_blank" rel="noopener">DBLP</a>
    <button class="pub-btn" data-toggle-bibtex="bib-sixdenier2021towards">BibTeX</button>
  </div>

  <div id="bib-sixdenier2021towards" class="bibtex-block">
    <button class="btn btn-secondary btn-sm copy-bibtex-btn" data-copy-target="bib-sixdenier2021towards" data-i18n="common.copy">Copy</button>
<code>@inproceedings{sixdenier2021towards,
  author    = {Sixdenier, Pierre-Louis},
  title     = {Towards an Autonomous, Power-Efficient Base Station for Sensor Data Collection},
  booktitle = {2021 2nd IEEE International Conference on Autonomic Computing and Self-Organizing Systems Companion (ACSOS-C)},
  year      = {2021},
  pages     = {246--249},
  doi       = {10.1109/ACSOS-C52956.2021.00083},
  publisher = {IEEE}
}</code>
  </div>
</article>
