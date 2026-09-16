/**
 * Pierre-Louis Sixdenier - Multilingual Translation Dictionary
 * English (EN), French (FR), German (DE)
 */

const TRANSLATIONS = {
  en: {
    // Navigation
    "nav.about": "About",
    "nav.experience": "Experience",
    "nav.education": "Education",
    "nav.publications": "Publications",
    "nav.projects": "Projects",
    "nav.skills": "Skills",
    "nav.resume_pdf": "Resume (PDF)",
    "nav.resume_pdf_link": "Resume (PDF) ↗",

    // Common / Actions
    "common.back_to_top": "Back to top",
    "common.copy": "Copy",
    "common.copied": "✓ BibTeX copied to clipboard!",
    "common.copy_error": "Error copying to clipboard",
    "common.view_papers": "View Papers",
    "common.download_bib": "Download papers.bib",

    // Hero Section
    "hero.status": "PhD Candidate &bull; Smart Electronic Systems &bull; Hardware/Software Co-Design",
    "hero.greeting": "Hi, I'm",
    "hero.tagline": "Computer Science & Embedded Systems Researcher &bull; PhD Candidate",
    "hero.btn_resume": "Resume (PDF)",
    "hero.btn_plain": "Plain B&amp;W View",
    "hero.btn_learn_more": "Learn More",
    "hero.stat_rank_val": "1st",
    "hero.stat_rank_label": "Master Rank (Smart Systems)",
    "hero.stat_hackathon_val": "2",
    "hero.stat_hackathon_label": "Hackathon Podiums",
    "hero.stat_projects_val": "5+",
    "hero.stat_projects_label": "Hardware &amp; IoT Projects",
    "hero.stat_toeic_val": "975",
    "hero.stat_toeic_label": "TOEIC Score (C1)",

    // Section Headers
    "section.about.badge": "Biography",
    "section.about.title": "About Me",
    "section.about.subtitle": "Embedded Systems Engineer & Computer Science Doctoral Student passionate about FPGA, neuromorphic hardware, and smart connected devices.",

    "section.experience.badge": "Career History",
    "section.experience.title": "Professional Experience",
    "section.experience.subtitle": "Industrial engineering positions, research lab internships, and professional appointments.",

    "section.education.badge": "Curriculum Vitae",
    "section.education.title": "Academic Background",
    "section.education.subtitle": "Formal higher education degrees, academic distinctions, and international exchange programs.",

    "section.publications.badge": "Research Output",
    "section.publications.title": "Scientific Papers & Publications",
    "section.publications.subtitle": "Peer-reviewed conference proceedings and workshop publications in embedded systems, energy-harvesting IoT, and hardware-software co-design.",

    "section.projects.badge": "Portfolio & Engineering",
    "section.projects.title": "Projects & Hardware Prototypes",
    "section.projects.subtitle": "Personal inventions, embedded IoT systems, and academic hardware/software research projects.",

    "section.skills.badge": "Expertise & Honors",
    "section.skills.title": "Skills, Languages & Recognitions",
    "section.skills.subtitle": "Technical competencies, embedded hardware tools, languages, and competitive hackathon achievements.",

    // About Section Content
    "about.p1": "I am a <strong>Computer Science &amp; Embedded Systems Engineer and PhD Student</strong>, specializing in <strong>Embedded Systems</strong>, <strong>FPGA Acceleration</strong>, <strong>Low-Power Platforms</strong>, and <strong>Smart Connected Systems</strong>.",
    "about.p2": "I completed my <strong>Master in Computer Science</strong> at <strong>CY Cergy Paris University</strong>, graduating top of my class in the research track for <em>Smart Electronic Systems</em>, following an exchange program at <strong>Oregon State University</strong> (USA) and a <strong>Licence in Computer Science</strong> with high honors from the <strong>University of Poitiers</strong>. My work spans hardware-software co-design, ranging from research on Spiking Neural Networks (SNN) on FPGA, failure detection systems for robotics (ETIS laboratory), to streaming IP debugging on low-power FPGAs at <strong>Safran Electronics &amp; Defense</strong>.",
    "about.interests_title": "🎯 Core Interests",
    "about.interest_1": "FPGA Architecture &amp; R&amp;D (VHDL, Vivado, Quartus)",
    "about.interest_2": "Embedded Systems &amp; Firmware (C/C++, STM32, Arduino)",
    "about.interest_3": "Neuromorphic Computing &amp; Spiking Neural Networks (SNN)",
    "about.interest_4": "Robotics, Sensor Fusion &amp; Driving Assistance Systems",
    "about.interest_5": "Low-Power Computing &amp; IoT Solutions",
    "about.contact_title": "📬 Contact Details",
    "about.contact_desc": "Feel free to reach out for research inquiries, technical discussions, or collaboration opportunities.",
    "about.nationality_label": "Nationality:",
    "about.nationality_val": "French",
    "about.email_label": "Email:",
    "about.phone_label": "Phone:",

    // Experience Items
    "exp.job.title": "[Job Title Placeholder &bull; e.g. PhD Researcher / R&amp;D Engineer]",
    "exp.job.period": "Nov 2020 &ndash; May 2026",
    "exp.job.org": "[Company / Research Institution Placeholder]",
    "exp.job.desc": "<em>[Placeholder: Describe your primary responsibilities, research topics, or engineering objectives during this period.]</em>",
    "exp.job.b1": "<strong>[Key Project / Thesis]:</strong> Detailed description of research or industrial project deliverables.",
    "exp.job.b2": "<strong>[Methodology &amp; Architecture]:</strong> Hardware/software co-design, prototyping, and algorithm implementation.",
    "exp.job.b3": "<strong>[Outcomes]:</strong> Publications, industrial patents, benchmarks, or deployed embedded platforms.",

    "exp.safran.title": "FPGA R&amp;D Engineer Intern",
    "exp.safran.period": "May 2020 &ndash; Nov 2020",
    "exp.safran.org": "Safran Electronics &amp; Defense",
    "exp.safran.desc": "Conception of a debugging streaming IP for an embedded low-power FPGA platform.",
    "exp.safran.b1": "Architected and implemented a custom streaming IP dedicated to non-intrusive live debugging on resource-constrained FPGAs.",
    "exp.safran.b2": "Optimized resource utilization, timing closure, and power consumption for defense and aerospace embedded requirements.",
    "exp.safran.b3": "Performed RTL simulation, verification testbenches, and on-board hardware validation.",

    "exp.etis.title": "Research Intern",
    "exp.etis.period": "December 2018",
    "exp.etis.org": "ETIS Laboratory (Equipes Traitement de l'Information et Systèmes)",
    "exp.etis.desc": "Conception and implementation of a failure detection system for robots.",
    "exp.etis.b1": "Investigated autonomous robotics anomaly detection algorithms based on sensor telemetry and internal state monitoring.",
    "exp.etis.b2": "Developed a real-time detection prototype to prevent robotic failure and ensure operational reliability.",

    "exp.xlim.title": "Research Intern",
    "exp.xlim.period": "June 2017",
    "exp.xlim.org": "XLIM-SIC Laboratory",
    "exp.xlim.desc": "Conception of a proof-of-concept (PoC) on an L-System (Lindenmayer system) generator.",
    "exp.xlim.b1": "Explored algorithmic procedural generation, rewriting grammars, and geometric visualization of fractals.",
    "exp.xlim.b2": "Implemented the generation engine and user interface for interactive rule testing.",

    // Education Items
    "edu.phd.title": "Doctor of Philosophy (Ph.D.) in Computer Science",
    "edu.phd.period": "2020 &ndash; 2026 (Expected)",
    "edu.phd.org": "[Doctoral School / Research Laboratory Placeholder]",
    "edu.phd.desc": "<strong>Thesis:</strong> <em>\"[PhD Dissertation Title Placeholder &bull; Embedded Systems / Hardware Computing / AI]\"</em>",
    "edu.phd.b1": "<strong>Advisors:</strong> [Advisor Names Placeholder]",
    "edu.phd.b2": "<strong>Specialization:</strong> Embedded Systems, Hardware Acceleration, Edge AI, Distributed Systems.",

    "edu.master.title": "Master in Computer Science",
    "edu.master.period": "2018 &ndash; 2020",
    "edu.master.org": "CY Cergy Paris University",
    "edu.master.desc": "<strong>Distinction:</strong> Top-ranking of the research program in <em>Smart Electronic Systems</em>.",
    "edu.master.b1": "Advanced curriculum covering embedded computing architectures, hardware description languages (VHDL), real-time operating systems, and smart electronic systems.",
    "edu.master.b2": "Conducted research projects on Spiking Neural Networks (SNN) on FPGA and intelligent sensor networks.",

    "edu.exchange.title": "Exchange Program in Computer Science",
    "edu.exchange.period": "2017 &ndash; 2018",
    "edu.exchange.org": "Oregon State University",
    "edu.exchange.desc": "International academic exchange program in the School of Electrical Engineering and Computer Science.",
    "edu.exchange.b1": "Followed advanced Computer Science coursework in algorithms, operating systems, and computer engineering.",
    "edu.exchange.b2": "Gave French lessons as a tutor to undergraduate students.",

    "edu.licence.title": "Licence in Computer Science",
    "edu.licence.period": "2015 &ndash; 2018",
    "edu.licence.org": "University of Poitiers",
    "edu.licence.desc": "<strong>Graduation:</strong> Graduated with high honors (Mention Bien / Très Bien).",
    "edu.licence.b1": "Comprehensive training in computer science fundamentals: algorithms, data structures, object-oriented programming (C++, C, Java), mathematics, and database management.",

    // Publications Banner & Abstracts
    "pub.indexed_in": "Publications indexed in <strong>IEEE Xplore</strong>, <strong>ACM Digital Library</strong>, and <strong>DBLP</strong>.",
    "pub.p1.abstract": "<strong>Abstract:</strong> Investigates early-exit deep neural network (EE-NN) architecture search tailored for edge computing platforms powered by intermittent energy harvesting, dynamically selecting confidence-based early exits to preserve accuracy under fluctuating ambient power.",
    "pub.p2.abstract": "<strong>Abstract:</strong> Proposes early-exit forecasting models allowing energy-harvesting edge sensors to anticipate the computational feasibility of inference branches across future harvesting windows.",
    "pub.p3.abstract": "<strong>Abstract:</strong> Introduces utility-aware transmission policies for battery-less or energy-harvesting IoT gateways, dynamically prioritizing high-entropy sensor streams over lossy wireless channels.",
    "pub.p4.abstract": "<strong>Abstract:</strong> Formulates GRES, a scheduling algorithm guaranteeing that embedded sensors maintain a reserved residual energy budget across uncertain solar/kinetic harvesting cycles through continuous task quality adaptation.",
    "pub.p5.abstract": "<strong>Abstract:</strong> Combines evolutionary genetic algorithms with deep reinforcement learning to synthesize verifiable, reactive run-time requirement enforcers for multi-processor systems-on-chip under safety constraints.",
    "pub.p6.abstract": "<strong>Abstract:</strong> Presents Seque, an ultra-lean data storage and compression engine designed for energy-constrained IoT edge gateways, eliminating redundant I/O transactions to maximize battery lifetime.",
    "pub.p7.abstract": "<strong>Abstract:</strong> Develops a reinforcement learning framework that synthesizes formally verifiable run-time enforcers for mixed-criticality multi-processor systems-on-chip.",
    "pub.p8.abstract": "<strong>Abstract:</strong> Introduces SIDAM, an automated multi-objective design space exploration tool evaluating heterogeneous sensor configurations and power conditioning circuits for energy-neutral operations.",
    "pub.p9.abstract": "<strong>Abstract:</strong> Examines architectures for self-sustaining solar/ambient-powered IoT base stations, presenting adaptive power management heuristics for uninterrupted sensor ingestion.",

    // Projects Section
    "projects.personal_title": "🔧 Personal Projects",
    "projects.smart_glasses.name": "Smart Glasses",
    "projects.smart_glasses.desc": "A wearable Heads-Up Display (HUD) built on an OLED screen mounted directly onto glasses. Communicates with an Android device via Bluetooth Low Energy (BLE) to deliver turn-by-turn navigation assistance in real time.",
    "projects.pollution.name": "Pollution Advisor",
    "projects.pollution.desc": "A crowdsourced environmental monitoring solution consisting of a compact sensor-equipped Arduino device paired with an Android mobile app to collect, map, and open-source real-time urban air pollution data.",
    "projects.foot_angle.name": "Foot Angle Detector",
    "projects.foot_angle.desc": "A therapeutic computer-vision Android application that calculates the biomechanical angle of a patient's foot placed on an ArUco calibration board, providing non-invasive diagnostic angles for medical and physical rehabilitation tracking.",
    "projects.academic_title": "🎓 Academic &amp; Research Projects",
    "projects.snn.name": "Spiking Neural Network on FPGA",
    "projects.snn.desc": "Research, RTL modeling, and hardware simulation of a biologically inspired Spiking Neural Network (SNN) architecture implemented on FPGA for low-power, neuromorphic spike-based computation.",
    "projects.smart_car.name": "“La futée” : Smart Car",
    "projects.smart_car.desc": "An intelligent advanced driver-assistance system (ADAS) that anticipates forward hazards, obstacles, and collision risks using multi-sensor inputs to issue proactive real-time driver warnings.",

    // Skills Section
    "skills.languages_title": "Programming Languages",
    "skills.embedded_title": "Embedded &amp; FPGA",
    "skills.dbms_title": "Databases &amp; DBMS",
    "skills.flow_title": "Programming Flow &amp; Tools",
    "skills.spoken_title": "Spoken Languages",
    "skills.spoken_fr": "<strong>French:</strong> Native",
    "skills.spoken_en": "<strong>English:</strong> C1 (IELTS: 7, TOEIC: 975)",
    "skills.spoken_es": "<strong>Spanish:</strong> B1",
    "skills.proud_title": "Proud Of &amp; Awards",
    "skills.award_1": "🥈 <strong>2nd Place:</strong> Renault Digital Hackathon 2019",
    "skills.award_2": "🥈 <strong>2nd Place:</strong> ENSEack 2020",

    // Footer
    "footer.rights": "All rights reserved. Built with Jekyll &amp; GitHub Pages.",
    "footer.subtitle": "Hosted on GitHub Pages &bull; Multilingual markdown academic resume"
  },

  fr: {
    // Navigation
    "nav.about": "À propos",
    "nav.experience": "Expérience",
    "nav.education": "Formation",
    "nav.publications": "Publications",
    "nav.projects": "Projets",
    "nav.skills": "Compétences",
    "nav.resume_pdf": "CV (PDF)",
    "nav.resume_pdf_link": "CV (PDF) ↗",

    // Common / Actions
    "common.back_to_top": "Haut de page",
    "common.copy": "Copier",
    "common.copied": "✓ BibTeX copié dans le presse-papier !",
    "common.copy_error": "Erreur lors de la copie",
    "common.view_papers": "Voir les publications",
    "common.download_bib": "Télécharger papers.bib",

    // Hero Section
    "hero.status": "Doctorant &bull; Systèmes Électroniques Intelligents &bull; Co-conception Matériel/Logiciel",
    "hero.greeting": "Bonjour, je suis",
    "hero.tagline": "Chercheur en Informatique &amp; Systèmes Embarqués &bull; Doctorant",
    "hero.btn_resume": "CV (PDF)",
    "hero.btn_plain": "Version N&amp;B Simple",
    "hero.btn_learn_more": "En savoir plus",
    "hero.stat_rank_val": "1er",
    "hero.stat_rank_label": "Major de Master (Systèmes Intelligents)",
    "hero.stat_hackathon_val": "2",
    "hero.stat_hackathon_label": "Podiums en Hackathon",
    "hero.stat_projects_val": "5+",
    "hero.stat_projects_label": "Projets Matériels &amp; IoT",
    "hero.stat_toeic_val": "975",
    "hero.stat_toeic_label": "Score TOEIC (C1)",

    // Section Headers
    "section.about.badge": "Biographie",
    "section.about.title": "À Propos de Moi",
    "section.about.subtitle": "Ingénieur en systèmes embarqués et doctorant en informatique, passionné par les architectures FPGA, le matériel neuromorphique et les objets connectés intelligents.",

    "section.experience.badge": "Parcours Professionnel",
    "section.experience.title": "Expérience Professionnelle",
    "section.experience.subtitle": "Postes d'ingénierie industrielle, stages en laboratoires de recherche académique et mandats professionnels.",

    "section.education.badge": "Curriculum Vitae",
    "section.education.title": "Formation Académique",
    "section.education.subtitle": "Diplômes universitaires supérieurs, distinctions d'excellence et programmes d'échange internationaux.",

    "section.publications.badge": "Production Scientifique",
    "section.publications.title": "Publications Scientifiques",
    "section.publications.subtitle": "Actes de conférences internationales à comité de lecture et ateliers de recherche en systèmes embarqués, IoT à récupération d'énergie et co-conception.",

    "section.projects.badge": "Portfolio &amp; Ingénierie",
    "section.projects.title": "Projets &amp; Prototypes Matériels",
    "section.projects.subtitle": "Inventions personnelles, systèmes IoT embarqués et projets de recherche matériels/logiciels académiques.",

    "section.skills.badge": "Compétences &amp; Distinctions",
    "section.skills.title": "Compétences, Langues &amp; Distinctions",
    "section.skills.subtitle": "Compétences techniques, outils pour matériel embarqué, langues vivantes et distinctions obtenues en hackathons.",

    // About Section Content
    "about.p1": "Je suis <strong>ingénieur en informatique &amp; systèmes embarqués et doctorant</strong>, spécialisé dans les <strong>systèmes embarqués</strong>, l'<strong>accélération sur FPGA</strong>, les <strong>plateformes basse consommation</strong> et les <strong>systèmes communicants intelligents</strong>.",
    "about.p2": "J'ai obtenu mon <strong>Master en Informatique</strong> à <strong>CY Cergy Paris Université</strong> en tant que major de promotion du parcours recherche en <em>Systèmes Électroniques Intelligents</em>, après une année d'échange à l'<strong>Oregon State University</strong> (États-Unis) et une <strong>Licence en Informatique</strong> mention Très Bien à l'<strong>Université de Poitiers</strong>. Mes travaux couvrent la co-conception matériel-logiciel, allant de la recherche sur les réseaux de neurones à impulsions (SNN) sur FPGA, la détection de pannes en robotique (laboratoire ETIS), jusqu'au débogage d'IP de streaming basse consommation chez <strong>Safran Electronics &amp; Defense</strong>.",
    "about.interests_title": "🎯 Domaines d'Intérêt",
    "about.interest_1": "Architecture FPGA &amp; R&amp;D (VHDL, Vivado, Quartus)",
    "about.interest_2": "Systèmes Embarqués &amp; Firmware (C/C++, STM32, Arduino)",
    "about.interest_3": "Calcul Neuromorphique &amp; Réseaux Spiking (SNN)",
    "about.interest_4": "Robotique, Fusion de Capteurs &amp; Systèmes ADAS",
    "about.interest_5": "Calcul Basse Consommation &amp; Solutions IoT",
    "about.contact_title": "📬 Coordonnées",
    "about.contact_desc": "N'hésitez pas à me contacter pour tout échange de recherche, opportunité technique ou projet de collaboration.",
    "about.nationality_label": "Nationalité :",
    "about.nationality_val": "Française",
    "about.email_label": "Email :",
    "about.phone_label": "Téléphone :",

    // Experience Items
    "exp.job.title": "[Poste Placeholder &bull; ex. Doctorant Chercheur / Ingénieur R&amp;D]",
    "exp.job.period": "Nov. 2020 &ndash; Mai 2026",
    "exp.job.org": "[Entreprise / Institut de Recherche Placeholder]",
    "exp.job.desc": "<em>[Placeholder : Décrivez vos responsabilités principales, sujets de recherche ou objectifs d'ingénierie sur cette période.]</em>",
    "exp.job.b1": "<strong>[Projet Clé / Thèse] :</strong> Description détaillée des livrables de recherche ou des réalisations industrielles.",
    "exp.job.b2": "<strong>[Méthodologie &amp; Architecture] :</strong> Co-conception matériel/logiciel, prototypage et implémentation d'algorithmes.",
    "exp.job.b3": "<strong>[Résultats] :</strong> Publications scientifiques, brevets industriels, bancs de test ou plateformes embarquées déployées.",

    "exp.safran.title": "Stagiaire Ingénieur R&amp;D FPGA",
    "exp.safran.period": "Mai 2020 &ndash; Nov. 2020",
    "exp.safran.org": "Safran Electronics &amp; Defense",
    "exp.safran.desc": "Conception d'une IP de streaming de débogage pour une plateforme FPGA embarquée basse consommation.",
    "exp.safran.b1": "Conception et implémentation d'une IP de streaming dédiée au débogage non intrusif en temps réel sur FPGA contraint en ressources.",
    "exp.safran.b2": "Optimisation des ressources matérielles, fermeture temporelle et réduction de consommation énergétique pour l'aéronautique et la défense.",
    "exp.safran.b3": "Simulations RTL, bancs de test de vérification et validation matérielle sur carte.",

    "exp.etis.title": "Stagiaire de Recherche",
    "exp.etis.period": "Décembre 2018",
    "exp.etis.org": "Laboratoire ETIS (Équipes Traitement de l'Information et Systèmes)",
    "exp.etis.desc": "Conception et implémentation d'un système de détection de défaillances pour robots.",
    "exp.etis.b1": "Étude d'algorithmes de détection d'anomalies pour robots autonomes basés sur la télémétrie de capteurs et l'état interne.",
    "exp.etis.b2": "Développement d'un prototype temps réel pour prévenir les défaillances robotiques et assurer la fiabilité opérationnelle.",

    "exp.xlim.title": "Stagiaire de Recherche",
    "exp.xlim.period": "Juin 2017",
    "exp.xlim.org": "Laboratoire XLIM-SIC",
    "exp.xlim.desc": "Conception d'une preuve de concept (PoC) d'un générateur de L-Systèmes (systèmes de Lindenmayer).",
    "exp.xlim.b1": "Exploration de la génération procédurale algorithmique, grammaires de réécriture et visualisation géométrique de fractales.",
    "exp.xlim.b2": "Développement du moteur de génération et d'une interface graphique pour le test interactif de règles.",

    // Education Items
    "edu.phd.title": "Doctorat en Informatique (Ph.D.)",
    "edu.phd.period": "2020 &ndash; 2026 (Prévu)",
    "edu.phd.org": "[École Doctorale / Laboratoire de Recherche Placeholder]",
    "edu.phd.desc": "<strong>Thèse :</strong> <em>« [Titre de la Thèse Placeholder &bull; Systèmes Embarqués / Accélération Matérielle / IA] »</em>",
    "edu.phd.b1": "<strong>Directeurs de thèse :</strong> [Noms des Directeurs Placeholder]",
    "edu.phd.b2": "<strong>Spécialisation :</strong> Systèmes embarqués, co-conception matériel/logiciel, Edge AI et systèmes distribués.",

    "edu.master.title": "Master en Informatique",
    "edu.master.period": "2018 &ndash; 2020",
    "edu.master.org": "CY Cergy Paris Université",
    "edu.master.desc": "<strong>Distinction :</strong> Major de promotion du parcours recherche en <em>Systèmes Électroniques Intelligents</em>.",
    "edu.master.b1": "Formation approfondie en architectures embarquées, langages de description matérielle (VHDL), systèmes d'exploitation temps réel et électronique intelligente.",
    "edu.master.b2": "Projets de recherche sur les réseaux de neurones impulsionnels (SNN) sur FPGA et les réseaux de capteurs intelligents.",

    "edu.exchange.title": "Programme d'Échange Universitaire en Informatique",
    "edu.exchange.period": "2017 &ndash; 2018",
    "edu.exchange.org": "Oregon State University",
    "edu.exchange.desc": "Séjour d'échange international au sein de l'École d'Ingénierie Électrique et Informatique (EECS).",
    "edu.exchange.b1": "Cours avancés d'algorithmique, systèmes d'exploitation et architecture des ordinateurs.",
    "edu.exchange.b2": "Enseignement de cours de français en tant que tuteur aux étudiants de premier cycle.",

    "edu.licence.title": "Licence en Informatique",
    "edu.licence.period": "2015 &ndash; 2018",
    "edu.licence.org": "Université de Poitiers",
    "edu.licence.desc": "<strong>Diplôme :</strong> Obtenu avec mention Très Bien.",
    "edu.licence.b1": "Formation fondamentale complète : algorithmique, structures de données, programmation orientée objet (C++, C, Java), mathématiques et bases de données.",

    // Publications Banner & Abstracts
    "pub.indexed_in": "Publications répertoriées sur <strong>IEEE Xplore</strong>, <strong>ACM Digital Library</strong> et <strong>DBLP</strong>.",
    "pub.p1.abstract": "<strong>Résumé :</strong> Étude de la recherche d'architectures neuronales à sorties précoces (EE-NN) adaptée aux nœuds périphériques alimentés par récupération intermittente d'énergie, garantissant la précision sous contrainte de puissance variable.",
    "pub.p2.abstract": "<strong>Résumé :</strong> Modèles de prévision des sorties anticipées permettant aux capteurs à récupération d'énergie d'anticiper la faisabilité computationnelle des branches d'inférence futures.",
    "pub.p3.abstract": "<strong>Résumé :</strong> Stratégies de transmission sensibles à l'utilité des données pour passerelles IoT sans batterie, priorisant les flux à haute entropie sur canaux sans fil instables.",
    "pub.p4.abstract": "<strong>Résumé :</strong> Algorithme d'ordonnancement GRES garantissant un budget résiduel d'énergie de sécurité pour capteurs ambiants via une adaptation dynamique de la qualité des tâches.",
    "pub.p5.abstract": "<strong>Résumé :</strong> Combinaison d'algorithmes génétiques et d'apprentissage par renforcement pour synthétiser des modules de contrôle d'exécution vérifiables sur architectures MPSoC.",
    "pub.p6.abstract": "<strong>Résumé :</strong> Moteur de stockage et compression de données ultra-léger Seque pour passerelles IoT contraintes, éliminant les accès I/O superflus pour maximiser l'autonomie.",
    "pub.p7.abstract": "<strong>Résumé :</strong> Framework d'apprentissage par renforcement synthétisant des modules de respect des exigences temps réel formellement vérifiables pour MPSoC à criticité mixte.",
    "pub.p8.abstract": "<strong>Résumé :</strong> Outil d'exploration d'espace de conception multi-objectifs SIDAM évaluant configurations de capteurs et circuits d'alimentation pour fonctionnement énergétiquement neutre.",
    "pub.p9.abstract": "<strong>Résumé :</strong> Architectures de stations de base IoT autonomes alimentées par énergie solaire/ambiante, avec heuristiques de gestion énergétique pour collecte ininterrompue.",

    // Projects Section
    "projects.personal_title": "🔧 Projets Personnels",
    "projects.smart_glasses.name": "Lunettes Intelligentes",
    "projects.smart_glasses.desc": "Affichage tête haute (HUD) sur écran OLED monté directement sur des lunettes, communicant avec un terminal Android via Bluetooth Low Energy (BLE) pour fournir un guidage étape par étape en temps réel.",
    "projects.pollution.name": "Conseiller Pollution",
    "projects.pollution.desc": "Solution participative de suivi environnemental associant un boîtier compact Arduino doté de capteurs à une application Android pour collecter et cartographier en open source la pollution de l'air urbain.",
    "projects.foot_angle.name": "Détecteur d'Angle du Pied",
    "projects.foot_angle.desc": "Application Android médicale de vision par ordinateur calculant l'angle biomécanique du pied placé sur une mire ArUco pour le diagnostic et le suivi en rééducation fonctionnelle.",
    "projects.academic_title": "🎓 Projets Académiques &amp; de Recherche",
    "projects.snn.name": "Réseau de Neurones Impulsionnels sur FPGA",
    "projects.snn.desc": "Recherche, modélisation RTL et simulation matérielle d'une architecture de réseau de neurones à impulsions (SNN) sur FPGA pour un calcul neuromorphique à ultra-basse consommation.",
    "projects.smart_car.name": "« La futée » : Véhicule Intelligent",
    "projects.smart_car.desc": "Système d'aide à la conduite avancée (ADAS) capable d'anticiper les dangers et obstacles de la route grâce à une fusion multicapteurs afin d'alerter le conducteur en temps réel.",

    // Skills Section
    "skills.languages_title": "Langages de Programmation",
    "skills.embedded_title": "Embarqué &amp; FPGA",
    "skills.dbms_title": "Bases de Données &amp; SGBD",
    "skills.flow_title": "Méthodes &amp; Outils de Dév.",
    "skills.spoken_title": "Langues Vivantes",
    "skills.spoken_fr": "<strong>Français :</strong> Langue maternelle",
    "skills.spoken_en": "<strong>Anglais :</strong> C1 (IELTS : 7, TOEIC : 975)",
    "skills.spoken_es": "<strong>Espagnol :</strong> B1",
    "skills.proud_title": "Distinctions &amp; Hackathons",
    "skills.award_1": "🥈 <strong>2e Place :</strong> Hackathon Renault Digital 2019",
    "skills.award_2": "🥈 <strong>2e Place :</strong> ENSEack 2020",

    // Footer
    "footer.rights": "Tous droits réservés. Conçu avec Jekyll &amp; GitHub Pages.",
    "footer.subtitle": "Hébergé sur GitHub Pages &bull; CV académique multilingue piloté par Markdown"
  },

  de: {
    // Navigation
    "nav.about": "Über mich",
    "nav.experience": "Erfahrung",
    "nav.education": "Ausbildung",
    "nav.publications": "Publikationen",
    "nav.projects": "Projekte",
    "nav.skills": "Kenntnisse",
    "nav.resume_pdf": "Lebenslauf (PDF)",
    "nav.resume_pdf_link": "Lebenslauf (PDF) ↗",

    // Common / Actions
    "common.back_to_top": "Nach oben",
    "common.copy": "Kopieren",
    "common.copied": "✓ BibTeX in die Zwischenablage kopiert!",
    "common.copy_error": "Fehler beim Kopieren",
    "common.view_papers": "Publikationen ansehen",
    "common.download_bib": "papers.bib herunterladen",

    // Hero Section
    "hero.status": "Doktorand &bull; Intelligente Elektronische Systeme &bull; Hardware/Software-Co-Design",
    "hero.greeting": "Hallo, ich bin",
    "hero.tagline": "Wissenschaftlicher Mitarbeiter in Informatik &amp; Eingebetteten Systemen &bull; Doktorand",
    "hero.btn_resume": "Lebenslauf (PDF)",
    "hero.btn_plain": "Einfache S/W-Ansicht",
    "hero.btn_learn_more": "Mehr erfahren",
    "hero.stat_rank_val": "1.",
    "hero.stat_rank_label": "Jahrgangsbester Master (Intelligente Systeme)",
    "hero.stat_hackathon_val": "2",
    "hero.stat_hackathon_label": "Hackathon-Podestplätze",
    "hero.stat_projects_val": "5+",
    "hero.stat_projects_label": "Hardware- &amp; IoT-Projekte",
    "hero.stat_toeic_val": "975",
    "hero.stat_toeic_label": "TOEIC-Ergebnis (C1)",

    // Section Headers
    "section.about.badge": "Biografie",
    "section.about.title": "Über Mich",
    "section.about.subtitle": "Ingenieur für Eingebettete Systeme & Doktorand der Informatik mit Leidenschaft für FPGAs, neuromorphe Hardware und intelligente vernetzte Systeme.",

    "section.experience.badge": "Beruflicher Werdegang",
    "section.experience.title": "Berufliche Erfahrung",
    "section.experience.subtitle": "Industrielle Entwicklungstätigkeiten, Forschungspraktika an Hochschullaboren und berufliche Stationen.",

    "section.education.badge": "Curriculum Vitae",
    "section.education.title": "Akademischer Werdegang",
    "section.education.subtitle": "Hochschulabschlüsse, akademische Spitzenleistungen und internationale Austauschprogramme.",

    "section.publications.badge": "Forschungsergebnisse",
    "section.publications.title": "Wissenschaftliche Publikationen",
    "section.publications.subtitle": "Begutachtete Konferenz- und Workshop-Beiträge zu eingebetteten Systemen, Energy-Harvesting-IoT und Hardware-Software-Co-Design.",

    "section.projects.badge": "Portfolio &amp; Entwicklung",
    "section.projects.title": "Projekte &amp; Hardware-Prototypen",
    "section.projects.subtitle": "Eigene Erfindungen, eingebettete IoT-Systeme und akademische Hardware/Software-Forschungsprojekte.",

    "section.skills.badge": "Kenntnisse &amp; Erfolge",
    "section.skills.title": "Kenntnisse, Sprachen &amp; Auszeichnungen",
    "section.skills.subtitle": "Fachliche Kompetenzen, Werkzeuge für Embedded-Hardware, Sprachen und Auszeichnungen bei Programmierwettbewerben.",

    // About Section Content
    "about.p1": "Ich bin <strong>Informatik- und Embedded-Systems-Ingenieur sowie Doktorand</strong>, spezialisiert auf <strong>Eingebettete Systeme</strong>, <strong>FPGA-Beschleunigung</strong>, <strong>Low-Power-Plattformen</strong> und <strong>intelligente vernetzte Systeme</strong>.",
    "about.p2": "Meinen <strong>Master in Informatik</strong> habe ich an der <strong>CY Cergy Paris Universität</strong> als Jahrgangsbester im Forschungsschwerpunkt <em>Intelligente Elektronische Systeme</em> abgeschlossen, im Anschluss an ein Auslandsstudium an der <strong>Oregon State University</strong> (USA) und einen <strong>Bachelor (Licence) in Informatik</strong> mit Auszeichnung an der <strong>Universität Poitiers</strong>. Meine Forschung umfasst das Hardware-Software-Co-Design, von Spiking Neural Networks (SNN) auf FPGAs über Fehlererkennung in der Robotik (ETIS-Labor) bis hin zum Debugging von Streaming-IPs für Low-Power-FPGAs bei <strong>Safran Electronics &amp; Defense</strong>.",
    "about.interests_title": "🎯 Kernbereiche",
    "about.interest_1": "FPGA-Architektur &amp; F&amp;E (VHDL, Vivado, Quartus)",
    "about.interest_2": "Eingebettete Systeme &amp; Firmware (C/C++, STM32, Arduino)",
    "about.interest_3": "Neuromorphes Rechnen &amp; Spiking Neural Networks (SNN)",
    "about.interest_4": "Robotik, Sensorfusion &amp; Fahrerassistenzsysteme",
    "about.interest_5": "Energieeffizientes Rechnen &amp; IoT-Lösungen",
    "about.contact_title": "📬 Kontaktdaten",
    "about.contact_desc": "Kontaktieren Sie mich gerne für Forschungsanfragen, fachlichen Austausch oder Kooperationen.",
    "about.nationality_label": "Nationalität:",
    "about.nationality_val": "Französisch",
    "about.email_label": "E-Mail:",
    "about.phone_label": "Telefon:",

    // Experience Items
    "exp.job.title": "[Platzhalter Stellenbezeichnung &bull; z.B. Doktorand / F&amp;E-Ingenieur]",
    "exp.job.period": "Nov. 2020 &ndash; Mai 2026",
    "exp.job.org": "[Unternehmen / Forschungsinstitut Platzhalter]",
    "exp.job.desc": "<em>[Platzhalter: Beschreiben Sie Ihre Hauptaufgaben, Forschungsthemen oder Entwicklungsziele in diesem Zeitraum.]</em>",
    "exp.job.b1": "<strong>[Schlüsselprojekt / Dissertation]:</strong> Detaillierte Beschreibung der Forschungsergebnisse oder industriellen Meilensteine.",
    "exp.job.b2": "<strong>[Methodik &amp; Architektur]:</strong> Hardware-Software-Co-Design, Prototyping und Algorithmenimplementierung.",
    "exp.job.b3": "<strong>[Ergebnisse]:</strong> Wissenschaftliche Veröffentlichungen, Patente, Benchmarks oder einsatzbereite Embedded-Plattformen.",

    "exp.safran.title": "F&amp;E-Praktikant FPGA",
    "exp.safran.period": "Mai 2020 &ndash; Nov. 2020",
    "exp.safran.org": "Safran Electronics &amp; Defense",
    "exp.safran.desc": "Konzeption einer Streaming-Debugging-IP für eine energieeffiziente eingebettete FPGA-Plattform.",
    "exp.safran.b1": "Entwurf und Implementierung einer echtzeitfähigen, nicht-invasiven Streaming-IP für ressourcenbeschränkte FPGAs.",
    "exp.safran.b2": "Optimierung von Ressourcenverbrauch, Timing-Closure und Leistungsaufnahme für Anforderungen in Luftfahrt und Verteidigung.",
    "exp.safran.b3": "RTL-Simulation, Testbench-Verifikation und Hardware-Validierung auf FPGA-Boards.",

    "exp.etis.title": "Forschungspraktikant",
    "exp.etis.period": "Dezember 2018",
    "exp.etis.org": "ETIS-Forschungslabor (Equipes Traitement de l'Information et Systèmes)",
    "exp.etis.desc": "Konzeption und Implementierung eines Fehlererkennungssystems für Roboter.",
    "exp.etis.b1": "Erforschung von Algorithmen zur Anomalieerkennung für autonome Roboter anhand von Sensortelemetrie und internen Zustandsdaten.",
    "exp.etis.b2": "Entwicklung eines echtzeitfähigen Prototyps zur Vermeidung von Systemausfällen und Sicherstellung hoher Betriebszuverlässigkeit.",

    "exp.xlim.title": "Forschungspraktikant",
    "exp.xlim.period": "Juni 2017",
    "exp.xlim.org": "XLIM-SIC Forschungslabor",
    "exp.xlim.desc": "Konzeption eines Proof-of-Concept (PoC) für einen L-System-Generator (Lindenmayer-Systeme).",
    "exp.xlim.b1": "Untersuchung algorithmischer prozeduraler Generierung, Ersetzungsgrammatiken und geometrischer Fraktal-Visualisierung.",
    "exp.xlim.b2": "Implementierung des Generierungskerns und einer grafischen Benutzeroberfläche zur interaktiven Regelüberprüfung.",

    // Education Items
    "edu.phd.title": "Doktor der Ingenieurwissenschaften (Ph.D.) in Informatik",
    "edu.phd.period": "2020 &ndash; 2026 (Voraussichtlich)",
    "edu.phd.org": "[Graduiertenschule / Forschungslabor Platzhalter]",
    "edu.phd.desc": "<strong>Dissertation:</strong> <em>„[Dissertationsthema Platzhalter &bull; Eingebettete Systeme / Hardware-Beschleunigung / KI]“</em>",
    "edu.phd.b1": "<strong>Betreuer:</strong> [Namen der Betreuer Platzhalter]",
    "edu.phd.b2": "<strong>Schwerpunkte:</strong> Eingebettete Systeme, Hardwarebeschleunigung, Edge AI und verteilte Systeme.",

    "edu.master.title": "Master in Informatik",
    "edu.master.period": "2018 &ndash; 2020",
    "edu.master.org": "CY Cergy Paris Universität",
    "edu.master.desc": "<strong>Auszeichnung:</strong> Jahrgangsbester des Forschungsschwerpunkts <em>Intelligente Elektronische Systeme</em>.",
    "edu.master.b1": "Fortgeschrittenes Curriculum zu Embedded-Architekturen, Hardwarebeschreibungssprachen (VHDL), Echtzeitbetriebssystemen und intelligenter Elektronik.",
    "edu.master.b2": "Forschungsprojekte zu Spiking Neural Networks (SNN) auf FPGAs und intelligenten Sensornetzwerken.",

    "edu.exchange.title": "Austauschprogramm Informatik",
    "edu.exchange.period": "2017 &ndash; 2018",
    "edu.exchange.org": "Oregon State University",
    "edu.exchange.desc": "Internationales Studienjahr an der School of Electrical Engineering and Computer Science (USA).",
    "edu.exchange.b1": "Teilnahme an vertiefenden Vorlesungen in Algorithmen, Betriebssystemen und Computertechnik.",
    "edu.exchange.b2": "Erteilung von Französischunterricht als Tutor für Bachelorstudenten.",

    "edu.licence.title": "Licence (Bachelor) in Informatik",
    "edu.licence.period": "2015 &ndash; 2018",
    "edu.licence.org": "Universität Poitiers",
    "edu.licence.desc": "<strong>Abschluss:</strong> Mit Prädikat 'Sehr Gut' (Mention Très Bien) abgeschlossen.",
    "edu.licence.b1": "Fundierte Informatikausbildung: Algorithmen, Datenstrukturen, objektorientierte Programmierung (C++, C, Java), Mathematik und Datenbanksysteme.",

    // Publications Banner & Abstracts
    "pub.indexed_in": "Publikationen gelistet in <strong>IEEE Xplore</strong>, <strong>ACM Digital Library</strong> und <strong>DBLP</strong>.",
    "pub.p1.abstract": "<strong>Kurzfassung:</strong> Erforschung von Architektursuchen für tiefe neuronale Netze mit vorzeitigen Ausgängen (EE-NN) für intermittierend mit Energy-Harvesting betriebene Edge-Geräte zur Genauigkeitssicherung bei variabler Energieverfügbarkeit.",
    "pub.p2.abstract": "<strong>Kurzfassung:</strong> Vorhersagemodelle für Early-Exits, die es Energy-Harvesting-Knoten ermöglichen, die Machbarkeit von Inferenzpfaden in künftigen Erntefenstern vorauszuberechnen.",
    "pub.p3.abstract": "<strong>Kurzfassung:</strong> Nutzenbewusste Datenübertragungsstrategien für batterielose IoT-Gateways mit dynamischer Priorisierung entropiereicher Sensordaten über verlustbehaftete Funkkanäle.",
    "pub.p4.abstract": "<strong>Kurzfassung:</strong> GRES-Scheduling-Algorithmus zur Gewährleistung eines verlässlichen Restenergiebudgets bei Energy-Harvesting-Sensoren durch kontinuierliche Qualitätsanpassung.",
    "pub.p5.abstract": "<strong>Kurzfassung:</strong> Kombination genetischer Algorithmen mit Reinforcement Learning zur Synthese verifizierbarer Laufzeit-Überwachungskomponenten auf MPSoCs unter Sicherheitsanforderungen.",
    "pub.p6.abstract": "<strong>Kurzfassung:</strong> Schlankes Speicher- und Kompressionssystem Seque für energiearme IoT-Edge-Gateways zur Minimierung redundanter E/A-Operationen und Verlängerung der Batterielaufzeit.",
    "pub.p7.abstract": "<strong>Kurzfassung:</strong> Reinforcement-Learning-Framework zur Synthese formal überprüfbarer Laufzeit-Enforcer für MPSoCs mit gemischter Kritikalität.",
    "pub.p8.abstract": "<strong>Kurzfassung:</strong> Automatisiertes Entwurfsraum-Explorationswerkzeug SIDAM zur Evaluierung heterogener Sensorkonfigurationen und Energieumwandlungsschaltungen für energieneutralen Betrieb.",
    "pub.p9.abstract": "<strong>Kurzfassung:</strong> Architekturen für autarke solarbetriebene IoT-Basisstationen mit adaptiven Energiemanagement-Heuristiken für lückenlose Datenerfassung.",

    // Projects Section
    "projects.personal_title": "🔧 Persönliche Projekte",
    "projects.smart_glasses.name": "Intelligente Brille",
    "projects.smart_glasses.desc": "Ein am Brillengestell montiertes OLED-Head-Up-Display (HUD), das über Bluetooth Low Energy (BLE) mit einem Android-Gerät kommuniziert, um Navigationshinweise in Echtzeit direkt im Sichtfeld anzuzeigen.",
    "projects.pollution.name": "Schadstoff- &amp; Umweltberater",
    "projects.pollution.desc": "Crowdsourcing-Plattform zur Umweltüberwachung: kompakte sensorbestückte Arduino-Hardware gekoppelt mit Android-App zur offenen Erfassung und Kartierung urbaner Luftverschmutzung.",
    "projects.foot_angle.name": "Fußwinkel-Detektor",
    "projects.foot_angle.desc": "Therapeutische Android-App mit Computer-Vision, die den biomechanischen Fußwinkel eines Patienten auf einer ArUco-Referenztafel berührungslos für Diagnostik und Reha berechnet.",
    "projects.academic_title": "🎓 Akademische &amp; Forschungsprojekte",
    "projects.snn.name": "Spiking Neural Network auf FPGA",
    "projects.snn.desc": "Erforschung, RTL-Modellierung und Hardware-Simulation eines biologisch inspirierten Spiking Neural Networks (SNN) auf FPGA für extrem energieeffizientes neuromorphes Rechnen.",
    "projects.smart_car.name": "„La futée“ : Intelligentes Auto",
    "projects.smart_car.desc": "Intelligentes Fahrerassistenzsystem (ADAS), das Gefahren und Hindernisse auf der Fahrbahn mithilfe integrierter Sensorfusion frühzeitig erkennt und den Fahrer in Echtzeit warnt.",

    // Skills Section
    "skills.languages_title": "Programmiersprachen",
    "skills.embedded_title": "Embedded &amp; FPGA",
    "skills.dbms_title": "Datenbanken &amp; DBMS",
    "skills.flow_title": "Entwicklungswerkzeuge &amp; Workflow",
    "skills.spoken_title": "Sprachkenntnisse",
    "skills.spoken_fr": "<strong>Französisch:</strong> Muttersprache",
    "skills.spoken_en": "<strong>Englisch:</strong> C1 (IELTS: 7, TOEIC: 975)",
    "skills.spoken_es": "<strong>Spanisch:</strong> B1",
    "skills.proud_title": "Auszeichnungen &amp; Hackathons",
    "skills.award_1": "🥈 <strong>2. Platz:</strong> Renault Digital Hackathon 2019",
    "skills.award_2": "🥈 <strong>2. Platz:</strong> ENSEack 2020",

    // Footer
    "footer.rights": "Alle Rechte vorbehalten. Erstellt mit Jekyll &amp; GitHub Pages.",
    "footer.subtitle": "Gehostet auf GitHub Pages &bull; Mehrsprachiger Markdown-Lebenslauf"
  }
};

// Export or attach to window
if (typeof window !== "undefined") {
  window.TRANSLATIONS = TRANSLATIONS;
}
