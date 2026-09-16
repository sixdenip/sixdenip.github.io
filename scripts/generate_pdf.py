#!/usr/bin/env python3
"""
Generate a black-and-white, clean and simple academic resume PDF
summarizing the webpage content for Pierre-Louis Sixdenier.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib import colors

def generate_pdf(output_path="assets/resume-pierre-louis-sixdenier.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 0.5 inch margins = 36 points for standard 1-2 page academic resume
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Pure Black and White Styles
    name_style = ParagraphStyle(
        'DocName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        alignment=1, # Center
        textColor=colors.black,
        textTransform='uppercase'
    )

    sub_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica',
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
        fontSize=10,
        leading=13,
        textColor=colors.black,
        spaceBefore=7,
        spaceAfter=2,
        textTransform='uppercase'
    )

    item_title_left = ParagraphStyle(
        'ItemTitleLeft',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11.5,
        textColor=colors.black
    )

    item_title_right = ParagraphStyle(
        'ItemTitleRight',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11.5,
        alignment=2,
        textColor=colors.black
    )

    item_sub_left = ParagraphStyle(
        'ItemSubLeft',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        textColor=colors.black
    )

    item_sub_right = ParagraphStyle(
        'ItemSubRight',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        alignment=2,
        textColor=colors.black
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.black,
        leftIndent=12,
        firstLineIndent=-8,
        spaceBefore=1,
        spaceAfter=1
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.black
    )

    def make_header_row(title_l, title_r, sub_l='', sub_r=''):
        data = [[Paragraph(title_l, item_title_left), Paragraph(title_r, item_title_right)]]
        if sub_l or sub_r:
            data.append([Paragraph(sub_l, item_sub_left), Paragraph(sub_r, item_sub_right)])
        t = Table(data, colWidths=[380, 160])
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
            HRFlowable(width='100%', thickness=0.75, color=colors.black, spaceBefore=1, spaceAfter=4)
        ]

    story = []

    # 1. Header (Black and White, Minimalist)
    story.append(Paragraph('Pierre-Louis Sixdenier', name_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph('PhD Candidate in Computer Science &amp; Artificial Intelligence', sub_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        'Paris, France &bull; pierre-louis.sixdenier@example.edu &bull; https://sixdenier.github.io &bull; github.com/sixdenier &bull; linkedin.com/in/pierre-louis-sixdenier',
        contact_style
    ))
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width='100%', thickness=1.2, color=colors.black, spaceBefore=2, spaceAfter=4))

    # 2. Education
    story.extend(make_section_divider('Education'))

    story.append(make_header_row(
        'Doctor of Philosophy (Ph.D.) in Computer Science',
        '2023 &ndash; Present (Exp. 2026)',
        'Vision &amp; Learning Laboratory &bull; Doctoral School',
        'Paris, France'
    ))
    story.append(Paragraph('&bull; <b>Thesis:</b> <i>Scalable Self-Supervised Representations for Multimodal Perception in Low-Resource Regimes</i>', bullet_style))
    story.append(Paragraph('&bull; <b>Advisors:</b> Prof. Jane Doe, Dr. Alex Martin &bull; <b>Honors:</b> Full National Doctoral Research Fellowship', bullet_style))
    story.append(Spacer(1, 3))

    story.append(make_header_row(
        'M.Sc. in Computer Science &amp; Artificial Intelligence',
        '2021 &ndash; 2023',
        'Institute of Technology &bull; Faculty of Sciences',
        'France'
    ))
    story.append(Paragraph('&bull; <b>Graduation:</b> Summa Cum Laude (Rank 1st / 85, GPA: 4.0/4.0) &bull; <b>Thesis:</b> Geometric Deep Learning for 3D Segmentation', bullet_style))
    story.append(Spacer(1, 3))

    story.append(make_header_row(
        'B.Sc. in Mathematics and Computer Science',
        '2018 &ndash; 2021',
        'University Faculty of Exact Sciences',
        'France'
    ))
    story.append(Paragraph('&bull; <b>Graduation:</b> First-Class Honors (Mention Tr&egrave;s Bien) &bull; Dean&#39;s Honor List across all semesters', bullet_style))
    story.append(Spacer(1, 4))

    # 3. Professional Experience
    story.extend(make_section_divider('Professional Experience'))

    story.append(make_header_row(
        'Graduate Research Assistant (PhD Candidate)',
        'Oct 2023 &ndash; Present',
        'Vision &amp; Learning Laboratory',
        'Paris, France'
    ))
    story.append(Paragraph('&bull; Investigated self-supervised pre-training objectives for visual representation learning and multimodal reasoning.', bullet_style))
    story.append(Paragraph('&bull; Scaled distributed training workflows across 64+ NVIDIA H100 GPUs using PyTorch FSDP and DeepSpeed.', bullet_style))
    story.append(Paragraph('&bull; Mentored 4 Master&#39;s and undergraduate students on machine learning research projects.', bullet_style))
    story.append(Spacer(1, 3))

    story.append(make_header_row(
        'Research Scientist Intern',
        'May 2024 &ndash; Sep 2024',
        'AI Research Labs (Multimodal Foundations)',
        'London, UK / Hybrid'
    ))
    story.append(Paragraph('&bull; Developed parameter-efficient fine-tuning and contrastive distillation algorithms for vision transformers.', bullet_style))
    story.append(Paragraph('&bull; Reduced inference latency by 38% while retaining 99.2% zero-shot accuracy across 12 vision benchmarks.', bullet_style))
    story.append(Paragraph('&bull; Filed 1 patent on token pruning mechanisms for streaming multimodal architectures.', bullet_style))
    story.append(Spacer(1, 3))

    story.append(make_header_row(
        'Graduate Teaching Fellow',
        'Sep 2022 &ndash; Jun 2023',
        'Department of Computer Science',
        'University Campus'
    ))
    story.append(Paragraph('&bull; Headed lab recitations for CS-401 Deep Learning (60 students) and CS-202 Algorithms &amp; Data Structures (120 students).', bullet_style))
    story.append(Spacer(1, 4))

    # 4. Selected Publications
    story.extend(make_section_divider('Selected Scientific Publications'))

    story.append(Paragraph(
        '<b>[1] Contrastive Representation Learning with Adaptive Geometry for Low-Resource Multimodal Tasks</b><br/>'
        '<b><u>Pierre-Louis Sixdenier</u></b>, Jane Doe, Alex Martin.<br/>'
        '<i>Advances in Neural Information Processing Systems (<b>NeurIPS 2025</b>)</i> &ndash; <b>Spotlight</b>',
        body_style
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph(
        '<b>[2] Token-Sparse Vision Transformers: Adaptive Computation for Real-Time Dense Prediction</b><br/>'
        'Lucas Bernard, <b><u>Pierre-Louis Sixdenier</u></b>, Elena Rossi, Jane Doe.<br/>'
        '<i>IEEE/CVF Conference on Computer Vision and Pattern Recognition (<b>CVPR 2025</b>)</i> &ndash; <b>Oral Presentation</b>',
        body_style
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph(
        '<b>[3] Provable Convergence Bounds for Gradient-Based Self-Distillation in Deep Ensembles</b><br/>'
        '<b><u>Pierre-Louis Sixdenier</u></b>, Alex Martin.<br/>'
        '<i>International Conference on Learning Representations (<b>ICLR 2024</b>)</i>',
        body_style
    ))
    story.append(Spacer(1, 4))

    # 5. Side Projects
    story.extend(make_section_divider('Side Projects &amp; Software Tooling'))

    story.append(Paragraph(
        '&bull; <b>FastVisionBench:</b> High-throughput benchmarking harness for few-shot representation quality across 18 datasets in &lt;15 min. (Python, PyTorch, Distributed)',
        bullet_style
    ))
    story.append(Paragraph(
        '&bull; <b>LatentManifold.js:</b> WebAssembly &amp; WebGL interactive 3D browser visualizer for t-SNE, UMAP, and PCA in real time. (TypeScript, Three.js, Wasm)',
        bullet_style
    ))
    story.append(Paragraph(
        '&bull; <b>AutoBibSync:</b> Automated CI tool synchronizing DBLP, arXiv, and Google Scholar into validated BibTeX collections. (Python CLI, GitHub Actions)',
        bullet_style
    ))
    story.append(Spacer(1, 4))

    # 6. Skills & Service
    story.extend(make_section_divider('Technical Skills &amp; Academic Service'))

    story.append(Paragraph(
        '<b>Technical Stack:</b> Python (Expert), C/C++, CUDA, PyTorch, JAX/Flax, DeepSpeed, FSDP, Linux, SLURM, Docker, Git, LaTeX.<br/>'
        '<b>Academic Service:</b> Reviewer for <b>NeurIPS</b> (2024, 2025), <b>CVPR</b> (2025), <b>ICLR</b> (2025); ECCV Workshop Co-Organizer.',
        body_style
    ))

    doc.build(story)
    print(f"Generated clean black-and-white resume PDF at: {output_path} ({os.path.getsize(output_path)} bytes)")

if __name__ == "__main__":
    generate_pdf()
