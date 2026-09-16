#!/usr/bin/env python3
"""
Generate a black-and-white, clean and simple academic resume PDF
summarizing the updated information from Pierre-Louis Sixdenier's CV
and including all indexed scientific papers.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib import colors

def generate_pdf(output_path="assets/resume-pierre-louis-sixdenier.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 0.45 in / 32 points margins for crisp academic resume
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=32,
        rightMargin=32,
        topMargin=28,
        bottomMargin=28
    )

    styles = getSampleStyleSheet()

    # Pure Black and White Styles
    name_style = ParagraphStyle(
        'DocName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=21,
        alignment=1,
        textColor=colors.black,
        textTransform='uppercase'
    )

    sub_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        alignment=1,
        textColor=colors.black
    )

    contact_style = ParagraphStyle(
        'DocContact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        alignment=1,
        textColor=colors.black
    )

    section_heading = ParagraphStyle(
        'SectionHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=colors.black,
        spaceBefore=5,
        spaceAfter=2,
        textTransform='uppercase'
    )

    item_title_left = ParagraphStyle(
        'ItemTitleLeft',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        textColor=colors.black
    )

    item_title_right = ParagraphStyle(
        'ItemTitleRight',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        alignment=2,
        textColor=colors.black
    )

    item_sub_left = ParagraphStyle(
        'ItemSubLeft',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=10,
        textColor=colors.black
    )

    item_sub_right = ParagraphStyle(
        'ItemSubRight',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        alignment=2,
        textColor=colors.black
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=colors.black,
        leftIndent=11,
        firstLineIndent=-8,
        spaceBefore=0.5,
        spaceAfter=0.5
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=colors.black
    )

    def make_header_row(title_l, title_r, sub_l='', sub_r=''):
        data = [[Paragraph(title_l, item_title_left), Paragraph(title_r, item_title_right)]]
        if sub_l or sub_r:
            data.append([Paragraph(sub_l, item_sub_left), Paragraph(sub_r, item_sub_right)])
        t = Table(data, colWidths=[390, 158])
        t.setStyle(TableStyle([
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        return t

    def make_section_divider(title):
        return [
            Paragraph(title, section_heading),
            HRFlowable(width='100%', thickness=0.75, color=colors.black, spaceBefore=1, spaceAfter=3)
        ]

    story = []

    # 1. Header (Black and White, Minimalist)
    story.append(Paragraph('Pierre-Louis SIXDENIER', name_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph('Embedded Systems Engineer &bull; PhD Candidate', sub_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        'Nationality: French &bull; pierre-louis.sixdenier@outlook.fr &bull; +33 6 80 48 91 43 &bull; github.com/sixdenip &bull; linkedin.com/in/pierre-louis-sixdenier',
        contact_style
    ))
    story.append(Spacer(1, 2))
    story.append(HRFlowable(width='100%', thickness=1.2, color=colors.black, spaceBefore=2, spaceAfter=3))

    # 2. Professional Experience
    story.extend(make_section_divider('Experience'))

    story.append(make_header_row(
        '[Job Title Placeholder &bull; e.g. PhD Researcher / R&amp;D Engineer]',
        'November 2020 &ndash; May 2026',
        '[Company / Research Institution / University Lab Placeholder]',
        'France'
    ))
    story.append(Paragraph('&bull; <i>[Placeholder for research activities, engineering deliverables, or doctoral thesis work between Nov 2020 &ndash; May 2026].</i>', bullet_style))
    story.append(Spacer(1, 2))

    story.append(make_header_row(
        'FPGA R&amp;D Engineer Intern',
        'May 2020 &ndash; Nov 2020',
        'Safran Electronics &amp; Defense',
        'France'
    ))
    story.append(Paragraph('&bull; Conception of a debugging streaming IP for an embedded low-power FPGA platform.', bullet_style))
    story.append(Spacer(1, 2))

    story.append(make_header_row(
        'Research Intern',
        'December 2018',
        'ETIS Laboratory (Equipes Traitement de l&#39;Information et Syst&egrave;mes)',
        'Cergy, France'
    ))
    story.append(Paragraph('&bull; Conception and implementation of a failure detection system for robots.', bullet_style))
    story.append(Spacer(1, 2))

    story.append(make_header_row(
        'Research Intern',
        'June 2017',
        'XLIM-SIC Laboratory',
        'Poitiers, France'
    ))
    story.append(Paragraph('&bull; Conception of a proof-of-concept (PoC) on an L-System generator.', bullet_style))
    story.append(Spacer(1, 3))

    # 3. Education
    story.extend(make_section_divider('Education'))

    story.append(make_header_row(
        'Doctor of Philosophy (Ph.D.) in Computer Science',
        '2020 &ndash; 2026 (Exp.)',
        '[Doctoral School / Research Lab Placeholder]',
        'France'
    ))
    story.append(Paragraph('&bull; Research in Embedded Systems, Hardware-Software Co-Design &amp; Energy-Harvesting Edge Computing.', bullet_style))
    story.append(Spacer(1, 2))

    story.append(make_header_row(
        'Master in Computer Science',
        '2018 &ndash; 2020',
        'CY Cergy Paris University',
        'Cergy, France'
    ))
    story.append(Paragraph('&bull; <b>Top-ranking of the research program in Smart Electronic Systems.</b> Advanced curriculum in FPGA, VHDL, and embedded systems.', bullet_style))
    story.append(Spacer(1, 2))

    story.append(make_header_row(
        'Exchange Program &bull; Computer Science',
        '2017 &ndash; 2018',
        'Oregon State University',
        'Corvallis, OR, USA'
    ))
    story.append(Paragraph('&bull; Followed CS classes and gave French lessons to undergraduate students.', bullet_style))
    story.append(Spacer(1, 2))

    story.append(make_header_row(
        'Licence in Computer Science',
        '2015 &ndash; 2018',
        'University of Poitiers',
        'Poitiers, France'
    ))
    story.append(Paragraph('&bull; Graduated with high honors.', bullet_style))
    story.append(Spacer(1, 3))

    # 4. Publications (From papers.bib)
    story.extend(make_section_divider('Publications (Peer-Reviewed)'))

    papers = [
        "<b>[1] Early-Exit Neural Architecture Search for Energy-Harvesting Edge Computing.</b><br/><b><u>P.-L. Sixdenier</u></b>, M. Deutel, J. Teich. <i>IEEE 18th Int. Symposium on Embedded Multicore/Many-core Systems-on-Chip (MCSoC 2025)</i>. <b>Best Paper Award</b>.",
        "<b>[2] Early-Exit Forecasting of Deep Neural Networks on Energy-Harvesting Edge Devices.</b><br/><b><u>P.-L. Sixdenier</u></b>, M. Deutel, S. Wildermann, J. Teich. <i>7th Int. Workshop on IoT, Edge, and Mobile for Embedded Machine Learning (ITEM @ ECML-PKDD 2026)</i>.",
        "<b>[3] WiP Paper: Utility-Aware Transmission of Sensor Data on Energy-Harvesting IoT Gateways.</b><br/><b><u>P.-L. Sixdenier</u></b>, J. Arockiaraj, S. Wildermann, J. Teich. <i>22nd Int. Conf. on Embedded Wireless Systems and Networks (EWSN 2025)</i>.",
        "<b>[4] GRES: Guaranteed Remaining Energy Scheduling of Energy-harvesting Sensors by Quality Adaptation.</b><br/><b><u>P.-L. Sixdenier</u></b>, S. Wildermann, J. Teich. <i>13th Mediterranean Conference on Embedded Computing (MECO 2024)</i>.",
        "<b>[5] Hybrid Genetic Reinforcement Learning for Generating Run-Time Requirement Enforcers.</b><br/>J. Spieck, <b><u>P.-L. Sixdenier</u></b>, K. Esper, S. Wildermann, J. Teich. <i>21st ACM-IEEE Int. Symposium on Formal Methods and Models for System Design (MEMOCODE 2023)</i>.",
        "<b>[6] Seque: Lean and Energy-aware Data Management for IoT Gateways.</b><br/><b><u>P.-L. Sixdenier</u></b>, S. Wildermann, M. Ottens, J. Teich. <i>IEEE Int. Conference on Edge Computing and Communications (EDGE 2023)</i>.",
        "<b>[7] RAVEN: Reinforcement Learning for Generating Verifiable Run-Time Requirement Enforcers for MPSoCs.</b><br/>K. Esper, J. Spieck, <b><u>P.-L. Sixdenier</u></b>, S. Wildermann, J. Teich. <i>4th Workshop on Next Generation Real-Time Embedded Systems (NG-RES 2023)</i>.",
        "<b>[8] SIDAM: A Design Space Exploration Framework for Multi-sensor Embedded Systems Powered by Energy Harvesting.</b><br/><b><u>P.-L. Sixdenier</u></b>, S. Wildermann, D. Ziegler, J. Teich. <i>SAMOS XXII (Springer LNCS 2022)</i>.",
        "<b>[9] Towards an Autonomous, Power-Efficient Base Station for Sensor Data Collection.</b><br/><b><u>P.-L. Sixdenier</u></b>. <i>2021 IEEE ACSOS-C</i>."
    ]

    for p in papers:
        story.append(Paragraph(p, body_style))
        story.append(Spacer(1, 1.5))

    story.append(Spacer(1, 2))

    # 5. Projects
    story.extend(make_section_divider('Projects'))
    story.append(Paragraph(
        '<b>Personal:</b> <b>Smart glasses</b> (OLED HUD + BLE Android app), <b>Pollution advisor</b> (Arduino sensor crowdsourcing), <b>Foot angle detector</b> (ArUco computer vision).<br/>'
        '<b>Academic:</b> <b>Spiking Neural Network on FPGA</b> (neuromorphic RTL modeling &amp; simulation), <b>&ldquo;La fut&eacute;e&rdquo; Smart Car</b> (ADAS predictive driving assistance).',
        body_style
    ))
    story.append(Spacer(1, 3))

    # 6. Skills & Recognitions
    story.extend(make_section_divider('Skills &amp; Recognitions'))
    story.append(Paragraph(
        '<b>Technical:</b> C++, C, VHDL, Python, Node.js, HTML/CSS &bull; <b>DBMS:</b> MongoDB, Neo4J, PostgreSQL, MySQL<br/>'
        '<b>Embedded &amp; FPGA:</b> Arduino, STM32 (Keil &micro;Vision), Vivado, Quartus &bull; <b>Tools:</b> Git, Docker, UML<br/>'
        '<b>Languages:</b> French (Native), English (C1 / IELTS: 7 / TOEIC: 975), Spanish (B1)<br/>'
        '<b>Proud of:</b> 2<sup>nd</sup> place at Renault Digital Hackathon 2019 &bull; 2<sup>nd</sup> place at ENSEack 2020',
        body_style
    ))

    doc.build(story)
    print(f"Generated clean black-and-white resume PDF at: {output_path} ({os.path.getsize(output_path)} bytes)")

if __name__ == "__main__":
    generate_pdf()
