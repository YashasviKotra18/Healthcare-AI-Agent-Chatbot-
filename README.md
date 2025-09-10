<img width="789" alt="image" src="https://github.com/user-attachments/assets/0ed7fbfe-d885-4119-b24d-c920d2784f1e">

Visit Here: https://carecompanionagent.web.app/


<img width="870" alt="image" src="https://github.com/user-attachments/assets/c6f2a5dc-93a4-412d-8948-fda6c32e1c03" />






## Table of Contents

- [Project Overview](#project-overview)
- [End-to-End Pipeline](#end-to-end-pipeline)
  - [Data Collection](#data-collection)
  - [Data Ingestion and Storage](#data-ingestion-and-storage)
  - [Data Cleaning and Transformation](#data-cleaning-and-transformation)
  - [Data Preparation for Training](#data-preparation-for-training)
  - [Model Training and Fine-Tuning](#model-training-and-fine-tuning)
  - [Model Evaluation](#model-evaluation)
  - [Real-Time Deployment and Monitoring](#real-time-deployment-and-monitoring)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Project Status](#project-status)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Project Overview
<img width="658" alt="image" src="https://github.com/user-attachments/assets/6b87a956-2a6b-4bab-9a79-da15f96ffe3c" />


The **AI Care Companion** project aims to develop a conversational AI system to assist with symptom assessment, chronic care management, and real-time healthcare consultations. This AI-powered virtual assistant addresses the demand for scalable healthcare support, especially in underserved areas. The model leverages data from medical datasets, such as **iCliniq**, **HealthcareMagic**, and **MIMIC-III**, to train a robust large language model (LLM) tailored for healthcare.

## Model Support Architecture (LLMOPS)
<img width="1441" alt="image" src="https://github.com/user-attachments/assets/210d4100-0b4c-4bfc-96df-7d347c0a3e0a" />

## End-to-End Pipeline

This project follows a structured pipeline for data handling, model training, deployment, and real-time monitoring. Each stage is essential for creating an effective and accurate healthcare AI model.
## DATA PIPELINE
<img width="1022" alt="image" src="https://github.com/user-attachments/assets/a0352634-5da7-44c0-8e4b-9da738748410" />

### 1. Data Collection

- **Sources**:
  - **iCliniq**: Contains patient inquiries and doctor responses.
  - **HealthcareMagic**: Medical consultations, symptoms, diagnoses, treatments.
  - **MIMIC-III**: Clinical notes and lab results.

### 2. Data Ingestion and Storage


- **Cloud Storage**: Centralized in Google Cloud Storage, where raw data is stored.
- **Data Version Control (DVC)**: Tracks dataset changes, ensuring integrity and reproducibility.

### 3. Data Cleaning and Transformation

- **Standardization**: Data is cleaned and standardized (lowercasing, removing special characters, tokenization).
- **Embedding and Vector Storage**: PubMed-BERT embeddings and Pinecone DB are used to preprocess text data for the AI model.
- **Transformation Tools**: Apache Beam pipelines on Google Dataflow clean and transform the data, and BigQuery structures it into unified datasets.

### 4. Data Preparation for Training
<img width="530" alt="image" src="https://github.com/user-attachments/assets/e2de2958-be81-4b0c-aadf-36eeda97914f">

4.5. Retrieval-Augmented Generation (RAG) and Graph-Based Knowledge Injection
<img width="855" alt="image" src="https://github.com/user-attachments/assets/3d2e4c9d-bec7-4368-b17c-e8d98c887c6a" />

Knowledge Graph Construction:

Patient interactions, medical entities, and clinical relations are extracted and linked using SpaCy, Neo4j, and PubMedBERT.

Builds a structured GraphDB (Neo4j) representing relationships among symptoms, diagnoses, medications, and care plans.

RAG Integration:

A hybrid retriever system combines vector similarity (Pinecone) and symbolic search (Neo4j Cypher queries) to fetch the most relevant context for each prompt.

Retrieved knowledge is injected into the prompt to ground the LLM responses in accurate, real-world healthcare data.

Query Pipeline:

Uses LangChain to orchestrate retrieval from Pinecone and Neo4j, format context, and invoke the LLM (BioMistral, MedLlama2, etc.) with enriched inputs.

Benefits:

Reduces hallucinations and improves clinical grounding.

Supports multihop reasoning using graph traversals (e.g., from symptom ➝ diagnosis ➝ treatment).



- **Dataset Splitting**: Data is split into training (80%), validation (10%), and test (10%) sets.
- **Storage Format**: Prepared data is stored in JSONL for compatibility with LLM training.
- **Performance Monitoring**: Continuous quality checks ensure data consistency for model training.
  

### 5. Model Training and Fine-Tuning
<img width="844" alt="image" src="https://github.com/user-attachments/assets/dedff621-13f6-457b-98c1-d68b851a96ca" />


- **Model Selection**: MedLlama2, BioMistral, Meditron, and MedAlpaca are fine-tuned on healthcare-specific data.
- **Techniques**: LoRA, LLMOps, and PEFT are used for efficient fine-tuning and optimization.
- **Framework**: Google Vertex AI and NVIDIA A100 GPUs ensure high-performance training.

### 6. Model Evaluation
<img width="1251" alt="image" src="https://github.com/user-attachments/assets/da501dce-3541-4c69-b8c6-1fafc1d37044" />


- **Metrics**: The model is evaluated based on AUC-ROC, F1 score, ROUGE, and latency.
- **Validation**: Ensures the model’s accuracy and relevance in healthcare consultations.
<img width="1199" alt="image" src="https://github.com/user-attachments/assets/ead4521a-4b4c-42b7-baee-a25b87bd3774" />

### 7. Real-Time Deployment and Monitoring

<img width="864" alt="image" src="https://github.com/user-attachments/assets/4e2e7b07-beea-41fe-8024-55bf08349c15" />


- **Deployment**: Fine-tuned models are deployed on Google Cloud Run for scalable, real-time healthcare responses.
- **Monitoring and Feedback**: Continuous model monitoring using Cloud Logging and Pub/Sub, which provide real-time performance feedback and allow for iterative improvement.

---


DEMO:
Use Case 1: Symptom Checker
<img width="931" alt="image" src="https://github.com/user-attachments/assets/6fe85594-b7a4-4338-8fbd-05bac52ee229" />

Use Case 2: Medical Information Access
<img width="954" alt="image" src="https://github.com/user-attachments/assets/2f567c99-97f8-4deb-b108-c225216b1054" />

Use Case 3: Healthcare Provider 
<img width="875" alt="image" src="https://github.com/user-attachments/assets/7a485842-27b9-40f9-a94b-f393703fc735" />




## Setup Instructions

### Prerequisites

- Google Cloud SDK and necessary permissions
- Python environment with required libraries (`Airflow`, `pandas`, etc.)
- Access to Google Cloud Storage, BigQuery, Vertex AI, and Cloud Composer

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/AI-Care-Companion.git
   cd AI-Care-Companion


