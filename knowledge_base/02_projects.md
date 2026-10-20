# Atchaya's Projects

## Automated Formulation
**Status:** Published Excel Add-in, currently in a team pilot
**Role:** Developer, under mentorship

Automated Formulation converts a BDD (Behaviour-Driven Development) Discovery Sheet, also called an Example Mapping document, into a Gherkin feature file used in software test automation.

**How it works:** Atchaya built a VSTO/C# Excel Add-in that reads the BDD Discovery Sheet from an Excel file. The content is passed to an internal enterprise LLM assistant using carefully engineered prompts. The LLM generates the Gherkin feature file, which is saved automatically to the desired location.

**Impact:** The tool reduced manual feature-file authoring effort by 14%, measured against the earlier manual process. It moved from proof of concept to a published, installable Excel Add-in and is being piloted across teams for feedback before wider rollout.

**Tech stack:** C#, VSTO, Excel Add-in framework, internal enterprise LLM, prompt engineering.

## MTKF (Governed Knowledge Platform)
**Status:** Ongoing, since January 2026
**Role:** Contributor. The platform architecture was designed by a senior architect, and Atchaya extended it.

MTKF is an AI platform for building citation-backed RAG assistants and agentic workflows on a shared ingestion and retrieval layer.

**Atchaya's contributions:**
- **Human handoff:** in the RAG assistant, a conversation is escalated to a person when the user asks for one, and a summary of the chat is passed along so the agent does not repeat questions.
- **Artifact generation:** assistant answers are turned into reports and documents drawn from the knowledge base.
- **Data-source connectors:** four connectors (a file server, ServiceNow, Azure DevOps and a generic REST API connector) that pull content into the ingestion pipeline.
- **Authentication and access control:** OIDC-based authentication and role-based access control (RBAC).

**Tech stack:** Python, FastAPI, React, TypeScript.

## Discovery Sheet Generator
**Status:** Proof of concept
**Role:** Developer

This is the reverse pipeline of Automated Formulation. It generates the BDD Discovery Sheet (Example Mapping) from raw requirements documents, using the same LLM-integration pattern and Excel Add-in approach.

**Impact:** Projected to reduce manual discovery-sheet creation effort by roughly 70% once adopted. This figure is based on early testing and has not been proven in production.

**Tech stack:** C#, VSTO, internal enterprise LLM, prompt engineering.

## GWP Assistant
**Status:** Proof of concept, demo-ready, paused due to budget
**Role:** Built the chatbot interface

GWP Assistant is a RAG-based chatbot connected to an internal enterprise knowledge base. It is scoped to Good Weighing Practice (GWP), a Mettler Toledo product line and methodology.

**How it works:** Atchaya built the chat interface in Angular. The chatbot connects to the internal knowledge base, which handles retrieval of relevant GWP documentation, and returns grounded answers to user questions about Good Weighing Practice.

**Status note:** The project reached demo-ready stage. Further work was paused because of internal budget constraints.

**Tech stack:** Angular, an internal enterprise knowledge base with vector search, internal enterprise LLM.

## Asset+ Summary Assistant
**Status:** Proof of concept, in progress
**Role:** Developer

An LLM-driven summarization tool for Asset+, a Mettler Toledo product. It generates readable summaries from structured assessment variables, reusing the LLM-integration pattern from Atchaya's earlier projects.

**Tech stack:** Internal enterprise LLM, prompt engineering, structured data processing.

## ServiceNow Prototype RAG Assistant
**Status:** Prototype built during a three-month internship (May–July 2024)
**Role:** Built independently as a technical exercise. It was not used in a project.

During her internship at ServiceNow's Software Development Center in Hyderabad, Atchaya built a prototype RAG assistant to demonstrate retrieval-augmented question answering.

**Tech stack:** Python, LangChain, ChromaDB, Hugging Face embeddings, an LLM API.

## The Common Pattern Across the Mettler Toledo Projects

Most of Atchaya's projects follow the same core pattern:

Structured input → LLM processing with engineered prompts → structured output

She has applied it to software test automation (BDD/Gherkin), requirements engineering, RAG-based knowledge retrieval, and data summarization.
