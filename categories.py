"""
This module defines the assessment categories and their associated questions.
Each category has a name, description, and a list of questions.
Each question has a text, type (likert or binary), weight, and maturity_hints.
The maturity_hints provide guidance on how to assess each level of maturity from 0 to 5.
"""

# Define the generic maturity scale descriptions
GENERIC_MATURITY_HINTS = {
    0: "Initial: No formal processes or capabilities exist.",
    1: "Basic: Ad-hoc processes with limited formalization and documentation.",
    2: "Developing: Processes are documented but inconsistently applied.",
    3: "Defined: Standard processes are defined and followed consistently.",
    4: "Managed: Processes are measured and controlled with quantitative data.",
    5: "Optimizing: Continuous improvement is embedded in the organization."
}

# Define the assessment categories and questions
CATEGORIES = {
    "people": {
        "name": "People",
        "description": "Assesses the organization's human resource capabilities, skills, and culture.",
        "questions": [
            {
                "id": "p1",
                "text": "How well does the organization develop employee skills?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "No formal employee development program exists.",
                    1: "Limited, reactive training provided only when necessary.",
                    2: "Basic training program exists but is inconsistently applied.",
                    3: "Structured training program with regular assessments.",
                    4: "Comprehensive development programs with measured effectiveness.",
                    5: "Industry-leading continuous development culture with personalized growth plans."
                }
            },
            {
                "id": "p2",
                "text": "How effective is knowledge sharing across teams?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "No knowledge sharing practices in place; information silos exist.",
                    1: "Ad-hoc knowledge sharing through informal channels.",
                    2: "Some documented knowledge but inconsistent sharing practices.",
                    3: "Formal knowledge sharing procedures and regular collaboration sessions.",
                    4: "Robust knowledge management systems with active participation.",
                    5: "Knowledge sharing deeply embedded in culture with advanced tools and practices."
                }
            },
            {
                "id": "p3",
                "text": "How would you rate leadership support for innovation?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "Leadership discourages or ignores innovation.",
                    1: "Leadership occasionally acknowledges innovation but provides little support.",
                    2: "Leadership verbally supports innovation but allocates few resources.",
                    3: "Leadership actively encourages innovation with dedicated resources.",
                    4: "Leadership champions innovation with substantial investment and recognition.",
                    5: "Leadership creates a transformative innovation culture that drives organizational strategy."
                }
            },
            {
                "id": "p4",
                "text": "Does the organization have clear career progression paths?",
                "type": "binary",
                "weight": 1.0,
                "maturity_hints": {
                    "Yes": "The organization has well-defined career pathways with clear advancement criteria, skill requirements, and development opportunities for employees at all levels.",
                    "No": "Career progression is undefined, inconsistent, or left to individual managers without formal structure or transparency."
                }
            },
            {
                "id": "p5",
                "text": "How engaged are employees in continuous improvement?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "Employees show no interest in or awareness of improvement opportunities.",
                    1: "A few employees occasionally suggest improvements.",
                    2: "Some teams participate in improvement initiatives when directed.",
                    3: "Most employees regularly contribute improvement ideas.",
                    4: "Employees actively lead improvement initiatives with measurable results.",
                    5: "Continuous improvement is part of everyone's daily work with innovative approaches."
                }
            }
        ]
    },
    "process": {
        "name": "Process",
        "description": "Evaluates the maturity of business processes, methodologies, and standardization.",
        "questions": [
            {
                "id": "pr1",
                "text": "How well are processes documented and standardized?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "No documentation of processes exists.",
                    1: "Basic process documentation exists but is outdated or incomplete.",
                    2: "Processes documented but with limited standardization across teams.",
                    3: "Well-documented standardized processes followed across the organization.",
                    4: "Comprehensive process documentation with regular reviews and updates.",
                    5: "Highly standardized processes with integrated documentation and automation."
                }
            },
            {
                "id": "pr2",
                "text": "To what extent are process improvements implemented systematically?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "Process improvements are never considered or implemented.",
                    1: "Process improvements made reactively only after major issues.",
                    2: "Some improvements made but without systematic approach.",
                    3: "Regular process improvement cycles with defined methodology.",
                    4: "Systematic improvement with quantifiable objectives and results.",
                    5: "Continuous improvement culture embedded in all processes with predictive capabilities."
                }
            },
            {
                "id": "pr3",
                "text": "How effective is the feedback loop for process adjustments?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "No feedback mechanisms exist for processes.",
                    1: "Feedback collected informally and rarely actioned.",
                    2: "Feedback mechanisms exist but are inconsistently applied.",
                    3: "Structured feedback systems with regular review cycles.",
                    4: "Comprehensive feedback systems with measurable improvements.",
                    5: "Real-time integrated feedback systems that drive continuous refinement."
                }
            },
            {
                "id": "pr4",
                "text": "Does the organization use metrics to monitor process effectiveness?",
                "type": "binary",
                "weight": 1.0,
                "maturity_hints": {
                    "Yes": "The organization has established key performance indicators (KPIs) for processes, regularly collects data, analyzes performance metrics, and uses this information to drive improvements.",
                    "No": "The organization does not measure process performance or collects limited metrics without systematic analysis or application to improvement efforts."
                }
            },
            {
                "id": "pr5",
                "text": "How well are processes aligned with business objectives?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "Processes exist in isolation with no connection to business goals.",
                    1: "Some processes loosely tied to business objectives but without clear alignment.",
                    2: "Basic alignment exists but with gaps in key areas.",
                    3: "Most processes are explicitly mapped to business objectives.",
                    4: "Comprehensive alignment with regular reviews to ensure continued relevance.",
                    5: "Perfect alignment where processes directly enable and accelerate business strategy."
                }
            }
        ]
    },
    "technology": {
        "name": "Technology Adoption",
        "description": "Measures how effectively the organization adopts and utilizes technology.",
        "questions": [
            {
                "id": "t1",
                "text": "How advanced is the technology infrastructure?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "Outdated, inadequate infrastructure with significant technical debt.",
                    1: "Basic infrastructure with minimal capabilities and frequent issues.",
                    2: "Standard infrastructure that meets basic needs but with limitations.",
                    3: "Modern infrastructure with good reliability and performance.",
                    4: "Advanced infrastructure with high resilience and scalability.",
                    5: "State-of-the-art infrastructure with cutting-edge capabilities and automation."
                }
            },
            {
                "id": "t2",
                "text": "To what extent are emerging technologies evaluated and adopted?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "No awareness or evaluation of emerging technologies.",
                    1: "Limited awareness but rarely evaluates new technologies.",
                    2: "Some evaluation of new technologies but slow adoption.",
                    3: "Regular evaluation process with methodical adoption approach.",
                    4: "Proactive monitoring and evaluation with successful adoption.",
                    5: "Leading-edge approach with innovative early adoption of beneficial technologies."
                }
            },
            {
                "id": "t3",
                "text": "How well does the technology integrate across systems?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "Completely siloed systems with no integration.",
                    1: "Minimal integration with mostly manual data transfers.",
                    2: "Some integration exists but with significant gaps.",
                    3: "Most major systems integrated with standardized interfaces.",
                    4: "Comprehensive integration with well-designed architecture.",
                    5: "Seamless integration across all systems with real-time data flow."
                }
            },
            {
                "id": "t4",
                "text": "Does the organization have a technology roadmap?",
                "type": "binary",
                "weight": 1.0,
                "maturity_hints": {
                    "Yes": "A comprehensive technology roadmap exists that outlines future technology needs, planned upgrades, transition timelines, and alignment with business strategy.",
                    "No": "No formal technology roadmap exists or planning is ad-hoc without a strategic long-term vision for technology evolution."
                }
            },
            {
                "id": "t5",
                "text": "How effectively are technology investments aligned with business needs?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "Technology investments made with no consideration of business needs.",
                    1: "Limited alignment with frequent mismatches between technology and business.",
                    2: "Basic alignment exists but with gaps in key areas.",
                    3: "Good alignment with most technology investments supporting business goals.",
                    4: "Strong alignment with clear business cases for all major investments.",
                    5: "Perfect alignment where technology investments directly enable business strategy and create competitive advantage."
                }
            }
        ]
    },
    "governance": {
        "name": "Governance",
        "description": "Assesses the organization's governance framework, policies, and compliance practices.",
        "questions": [
            {
                "id": "g1",
                "text": "How clear are the organization's governance policies?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "No formal governance policies exist.",
                    1: "Minimal policies exist but are unclear or incomplete.",
                    2: "Basic policies exist but lack detail or comprehensive coverage.",
                    3: "Clear policies exist covering most governance areas.",
                    4: "Comprehensive, well-documented policies with regular reviews.",
                    5: "Exemplary policies that are clear, comprehensive, and adaptive to changing needs."
                }
            },
            {
                "id": "g2",
                "text": "To what extent is governance integrated into daily operations?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "Governance is completely disconnected from operations.",
                    1: "Minimal integration with governance seen as an overhead.",
                    2: "Some integration but often bypassed in practice.",
                    3: "Good integration with governance embedded in key processes.",
                    4: "Strong integration with governance as a natural part of operations.",
                    5: "Complete integration where governance enhances rather than restricts operations."
                }
            },
            {
                "id": "g3",
                "text": "How effective is risk management?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "No formal risk management exists.",
                    1: "Reactive approach to risks after they materialize.",
                    2: "Basic risk identification but limited mitigation planning.",
                    3: "Structured risk management process with regular reviews.",
                    4: "Comprehensive risk management with quantitative assessment.",
                    5: "Proactive, integrated risk management that drives strategic decisions."
                }
            },
            {
                "id": "g4",
                "text": "Does the organization have a formal compliance program?",
                "type": "binary",
                "weight": 1.0,
                "maturity_hints": {
                    "Yes": "A formal compliance program exists with clear policies, regular training, monitoring mechanisms, designated responsibilities, and reporting procedures.",
                    "No": "No formal compliance program exists, or compliance activities are ad-hoc and not organized into a coherent program."
                }
            },
            {
                "id": "g5",
                "text": "How well are governance responsibilities communicated and understood?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "Governance responsibilities are not defined or communicated.",
                    1: "Limited communication with poor understanding across the organization.",
                    2: "Basic responsibilities communicated but understanding varies greatly.",
                    3: "Clear communication with good understanding by most stakeholders.",
                    4: "Comprehensive communication program with verification of understanding.",
                    5: "Universal understanding where all employees can articulate their governance responsibilities."
                }
            }
        ]
    },
    "data": {
        "name": "Data Management",
        "description": "Evaluates how the organization collects, manages, and utilizes data.",
        "questions": [
            {
                "id": "d1",
                "text": "How mature is the organization's data management strategy?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "No data management strategy exists.",
                    1: "Basic ad-hoc approach to data management with no formal strategy.",
                    2: "Partial strategy exists but lacks comprehensiveness or implementation.",
                    3: "Formal strategy covers most aspects of data management.",
                    4: "Comprehensive strategy with clear objectives and implementation plans.",
                    5: "Advanced strategy that drives competitive advantage with continuous evolution."
                }
            },
            {
                "id": "d2",
                "text": "To what extent is data quality monitored and maintained?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "No data quality monitoring exists.",
                    1: "Quality issues addressed reactively when problems arise.",
                    2: "Basic quality checks but inconsistent application.",
                    3: "Regular data quality monitoring with established standards.",
                    4: "Comprehensive quality framework with automated monitoring.",
                    5: "Proactive quality management with predictive capabilities and continuous improvement."
                }
            },
            {
                "id": "d3",
                "text": "How effectively is data used for decision-making?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "Decisions made without consideration of data.",
                    1: "Limited use of data, primarily anecdotal or selective.",
                    2: "Some decisions supported by data but inconsistently applied.",
                    3: "Most major decisions informed by relevant data analysis.",
                    4: "Data-driven culture with comprehensive analytics supporting decisions.",
                    5: "Advanced analytics including predictive models driving strategic decisions."
                }
            },
            {
                "id": "d4",
                "text": "Does the organization have defined data governance policies?",
                "type": "binary",
                "weight": 1.0,
                "maturity_hints": {
                    "Yes": "Formal data governance policies exist that define data ownership, quality standards, access controls, privacy requirements, and lifecycle management.",
                    "No": "No formal data governance policies exist, or they are inconsistent, incomplete, or not formally adopted."
                }
            },
            {
                "id": "d5",
                "text": "How well is data security and privacy maintained?",
                "type": "likert",
                "weight": 1.0,
                "maturity_hints": {
                    0: "No data security or privacy measures in place.",
                    1: "Basic security measures but significant gaps or inconsistencies.",
                    2: "Standard security measures in place but reactive approach.",
                    3: "Good security framework with regular assessments and updates.",
                    4: "Comprehensive security program with proactive monitoring and incident response.",
                    5: "State-of-the-art security with advanced threat detection, privacy by design, and continuous adaptation."
                }
            }
        ]
    }
}

# Define category descriptions for results interpretation
MATURITY_LEVELS = {
    0: "Initial: Ad hoc and chaotic processes with little formalization.",
    1: "Managed: Processes are planned and executed according to policy.",
    2: "Defined: Processes are well characterized and understood.",
    3: "Quantitatively Managed: Processes are measured and controlled.",
    4: "Optimizing: Focus on continuous process improvement.",
    5: "Excellence: Best-in-class capabilities with innovative approaches."
}

# Helper function to get all question IDs
def get_all_question_ids():
    """Returns a list of all question IDs across all categories."""
    question_ids = []
    for category_id, category in CATEGORIES.items():
        for question in category["questions"]:
            question_ids.append(question["id"])
    return question_ids
