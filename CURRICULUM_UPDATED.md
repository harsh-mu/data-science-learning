# Technical Depth Curriculum

## Purpose of This Document

This document is the source of truth for Harsh Munagekar's long-term technical learning program. It is designed to be uploaded into a new ChatGPT conversation so that the new conversation immediately understands:

- why this curriculum exists;
- Harsh's current strengths and weaknesses;
- the learning philosophy to use;
- how each topic should be taught;
- what projects should be completed;
- what "learned" actually means;
- where the curriculum is heading after the initial data science phase.

This is intentionally a living document. Topics, projects, and completion status should be updated as Harsh progresses.

---

# 1. North Star

The central question for this curriculum is:

> **If AI/LLMs disappeared tomorrow, could Harsh independently implement, explain, debug, interpret, and eventually choose these techniques without relying on an LLM?**

The goal is not to become good at prompting an AI to produce technical work. The goal is to develop genuine subject-matter expertise and implementation fluency.

Long-term success means Harsh can:

- open a blank notebook/editor and independently begin solving a technical problem;
- understand code written by other data scientists and engineers;
- implement common statistical and machine-learning techniques without needing an LLM to generate the solution;
- explain how and why the techniques work;
- interpret model and statistical outputs correctly;
- debug implementations and reason about unexpected results;
- discuss technical work fluently with data scientists, ML engineers, AI engineers, quantitative/risk professionals, and interviewers;
- eventually determine which technique is appropriate for an unfamiliar problem and defend that choice;
- use documentation, libraries, and normal engineering resources without becoming dependent on generated solutions.

Technical interview fluency is an important outcome, but it is not the only outcome. The larger objective is **independent technical competence**.

---

# 2. Why This Curriculum Exists

Harsh has spent significant time learning technical concepts through conversations with AI. These sessions are useful for intuition and short-term understanding, but they have exposed a major weakness: **recognition is not recall, and recall is not implementation ability**.

It is easy to hear an explanation of neural networks, regression, RAG, agents, statistical testing, or another technical subject and think, "That makes sense." It is much harder to reproduce the idea days later, implement it from a blank file, explain it under interview pressure, or recognize when it should be used.

The curriculum therefore moves away from primarily conversational learning and toward:

> **Refresh -> Understand -> Implement -> Interpret -> Explain -> Recall -> Revisit**

Later, once the toolbox is strong enough, the curriculum expands to:

> **Problem -> Select -> Implement -> Compare -> Defend**

The project itself is part of the learning process. Projects are not something Harsh waits to do until after he has "finished learning" a topic.

---

# 3. Instructions for ChatGPT / Future Tutors

Any ChatGPT conversation using this curriculum should follow these rules unless Harsh explicitly asks to change the approach.

## 3.1 Do not begin with blind model selection

During the initial learning phase, do **not** hand Harsh an unfamiliar dataset and ask him to determine which statistical test or model to use.

That skill matters later, but it is not the immediate objective.

Initially, explicitly identify the technique being learned. Example:

> "This is the Linear Regression project. We are going to use linear regression on this dataset."

The immediate goal is to develop implementation and conceptual fluency with the individual tools before testing whether Harsh can select among them.

## 3.2 Begin each topic with a focused refresh

Before the project, spend roughly 30 minutes (flexible depending on complexity) refreshing the relevant knowledge.

The refresh should answer questions such as:

- What is this technique?
- What problem does it solve?
- What is the intuition behind it?
- How does it work at a high level?
- What mathematics is important?
- What does the input data need to look like?
- What preprocessing may be required?
- What assumptions does it make?
- What outputs does it produce?
- How are those outputs interpreted?
- What metrics should be used?
- What commonly goes wrong?
- Which Python libraries/functions are normally used?

The mathematical depth should generally be a mixture of:

**A. Intuition and enough mathematics to explain the concept**, and

**B. Understanding the important formulas well enough to manually calculate simple examples.**

Full mathematical derivations are not required for every technique.

## 3.3 Use from-scratch implementation selectively

Do not reimplement every production algorithm from scratch.

Hand implementation should be used when it exposes important mechanics that libraries otherwise hide.

Examples that are particularly valuable to implement in simplified form include:

- linear regression;
- logistic regression;
- K-nearest neighbors;
- K-means;
- PCA;
- a simplified decision tree;
- a basic neural network / backpropagation.

For statistical tests such as t-tests, chi-square, and ANOVA, manually calculate small examples so Harsh understands where the test statistic comes from. The actual project should still use established libraries such as SciPy or statsmodels.

Do **not** waste time rebuilding complex production implementations such as XGBoost or optimized SVM solvers unless there is a specific educational reason.

## 3.4 Production libraries are expected

Actual projects should teach the tools used in real work, including as appropriate:

- Python;
- pandas;
- NumPy;
- SciPy;
- statsmodels;
- scikit-learn;
- XGBoost;
- Matplotlib / Plotly;
- PyTorch;
- relevant APIs and data libraries.

Using a library is not cheating. The objective is to understand what the library is doing and be able to use it independently.

## 3.5 Do not write the entire solution for Harsh

Harsh should do the majority of implementation himself.

It is acceptable and encouraged to:

- explain concepts;
- refresh syntax;
- explain documentation;
- help diagnose errors;
- review an implementation;
- give hints;
- explain why something is incorrect;
- discuss alternative approaches.

Avoid simply generating the entire notebook/project unless Harsh explicitly requests it for a different purpose.

Documentation lookup, Google/search, Stack Overflow, official docs, and other normal engineering resources are allowed. The goal is independence from **LLM-generated solutions**, not artificial memorization of every API signature.

## 3.6 Interview Harsh after projects

After a project is complete, test conceptual and implementation understanding.

Questions should include both explanation and coding questions, such as:

- Explain the technique in your own words.
- Why does it work?
- What assumptions does it make?
- How did you prepare the data?
- What do the outputs mean?
- Why did you use the chosen evaluation metric?
- What could cause the model/test to fail?
- What would you try next?
- Reproduce the basic implementation from memory.

Do not simply quiz trivia. Test whether Harsh can reason about the technique.

## 3.7 Use delayed recall

Completed topics should periodically reappear after days or weeks.

Examples:

- explain linear regression again before starting random forests;
- write a basic train/test/model/predict/evaluate workflow from memory;
- explain the difference between a t-test and ANOVA;
- reproduce a simple logistic regression implementation without opening the old notebook.

The objective is long-term retention rather than short-term completion.

## 3.8 Model selection comes later

After Harsh has implemented and understood a meaningful set of tools, introduce unknown problems where he must determine:

1. What kind of problem is this?
2. What techniques are appropriate?
3. What assumptions matter?
4. Which models/tests should be tried?
5. How should they be evaluated?
6. Which approach is preferable for this specific objective?
7. How can that choice be defended?

This is a later stage of the curriculum, not the starting point.

---

# 4. Current Technical Baseline

This section is context for future conversations. It is not meant as a permanent assessment; update it as skills improve.

## Programming / Data

Harsh has practical Python and SQL experience and has previously used pandas, NumPy, SciPy, scikit-learn, statsmodels, Streamlit, Plotly, Power BI, databases, Docker, and Kubernetes.

However, some implementation knowledge has become rusty because many concepts have not been repeatedly implemented from scratch. NumPy and object-oriented programming have been used before but currently need reinforcement. Plotting is familiar but not highly fluent.

SQL is currently considered sufficiently comfortable and should remain outside this curriculum for now. It can have its own curriculum/course if needed later.

Python, NumPy, OOP, plotting, and general coding fluency should largely be strengthened organically through the projects rather than delaying the curriculum for a separate fundamentals course.

## Statistics / Data Science

Harsh has previously used or studied techniques including:

- t-tests;
- chi-square tests;
- Cramer's V;
- ANOVA;
- Tukey HSD;
- linear/logistic regression concepts;
- Z-scores;
- Theil's U;
- PCA;
- clustering prototypes;
- general statistical analysis.

Several of these were used during prior analytics work, but the current goal is to rebuild them with much greater independent implementation and explanation ability.

## Neural Networks / PyTorch

Harsh understands the broad conceptual flow:

- input data enters a network;
- layers transform representations using weights and biases;
- activation functions introduce nonlinearity;
- the output layer produces the required output/probabilities;
- a loss function measures error;
- backpropagation computes gradients;
- optimization adjusts weights.

However, implementation fluency and deeper interview-level explanation are not yet strong enough. Neural networks will therefore be revisited through both a simplified from-scratch implementation and PyTorch projects.

## AI Engineering

Harsh has conceptual exposure to:

- LLMs and tokenization;
- embeddings;
- vector databases;
- RAG;
- tool/function calling;
- agents;
- multi-agent systems;
- agent memory/state;
- MCP;
- context engineering;
- APIs.

The primary weakness is not conceptual recognition but independent implementation depth. **After the current Regression module is completed, AI / FDE engineering becomes the primary curriculum track.** Broader data science, statistics, and classical machine learning remain important, but they become a deliberately interleaved secondary track rather than prerequisites that must all be completed before AI engineering begins.

## Quantitative Finance / Trading / Risk

Harsh is interested in commodities, trading, risk analytics, markets, stochastic processes, volatility, derivatives, forecasting, and related quantitative topics.

This is not the immediate primary curriculum, but datasets involving commodities, energy, stocks, pricing, risk, or markets should be used where they naturally fit the statistical/ML objective. This allows projects to build both modeling skill and market intuition.

A dedicated quantitative finance/risk track comes later.

---

# 5. Standard Learning Workflow for Every Technique

Each major technique should progress through the following stages.

## Stage 1 - Refresh

Before coding, review:

- definition;
- intuition;
- problem type;
- important mathematics;
- assumptions;
- data requirements;
- preprocessing;
- outputs;
- interpretation;
- evaluation;
- common mistakes;
- relevant libraries.

**Goal:** Bring the topic into working memory before implementation.

## Stage 2 - Mechanics / From Scratch

Where educationally useful:

- manually calculate a tiny example; and/or
- implement a simplified version with basic Python/NumPy.

**Goal:** Understand what the library call hides.

This stage can be skipped when a from-scratch implementation adds little educational value.

## Stage 3 - Real Project

Use a real or realistic dataset and production libraries.

Typical workflow:

```text
Load data
    ->
Inspect / clean
    ->
Explore
    ->
Prepare features
    ->
Apply technique / train model
    ->
Evaluate
    ->
Interpret
    ->
Visualize where useful
```

The exact workflow changes by technique.

**Goal:** Independently perform the actual analysis/modeling workflow.

## Stage 4 - Write-Up

In Harsh's own words, document:

- What problem was solved?
- What does the technique do?
- Why was it appropriate for this project?
- What preprocessing was required?
- What happened?
- How should the result be interpreted?
- What assumptions or limitations matter?
- What mistakes/confusion occurred?
- What should be remembered in six months?

**Goal:** Force understanding through explanation and create a reusable knowledge base.

## Stage 5 - Technical Interview / Defense

ChatGPT asks conceptual, practical, and coding questions without Harsh relying heavily on the completed notebook.

**Goal:** Convert project familiarity into explainable technical knowledge.

## Stage 6 - Delayed Recall

Revisit the technique later without advance preparation.

**Goal:** Test retention.

## Stage 7 - Applied Selection (Later)

After enough techniques are individually strong, solve unfamiliar problems without being told which method to use.

**Goal:** Develop model/test selection and professional judgment.

---

# 6. Definition of "Learned"

A topic should not be marked complete simply because a notebook ran successfully.

Suggested status system:

- [ ] Not Started
- [ ] Refreshed
- [ ] Mechanics Understood / From-Scratch Exercise Completed
- [ ] Library Project Completed
- [ ] Write-Up Completed
- [ ] Interview / Defense Passed
- [ ] Delayed Recall Passed
- [ ] Applied Independently in a New Context

The final stage is the strongest evidence of mastery.

---

# 7. Phase I - Statistical Foundations and Inference

The initial curriculum begins here because these concepts underpin much of data science and have direct overlap with Harsh's previous work.

## 7.1 Descriptive Statistics and Distributions

### Topics

- mean, median, mode;
- variance and standard deviation;
- covariance;
- percentiles / quantiles;
- skewness;
- distributions;
- normal distribution;
- z-scores;
- sampling;
- population vs sample;
- Central Limit Theorem;
- standard error;
- confidence intervals.

### Project idea

Analyze a real dataset—preferably market, commodity, operations, or business data—and build a statistical profile of important variables.

### Implementation emphasis

Use pandas/NumPy but manually calculate selected statistics once.

---

## 7.2 Hypothesis Testing Fundamentals

### Topics

- null and alternative hypotheses;
- test statistics;
- p-values;
- significance level;
- confidence intervals;
- Type I error;
- Type II error;
- statistical significance vs practical significance;
- effect size;
- statistical power;
- one-tailed vs two-tailed tests.

This is conceptual infrastructure for the following tests.

---

## 7.3 One-Sample and Two-Sample t-Tests

### Learn

- what a t-test measures;
- independent vs paired samples;
- means and sampling distributions;
- standard error;
- t-statistic;
- degrees of freedom;
- equal vs unequal variance / Welch's t-test;
- p-value interpretation;
- Cohen's d / effect size;
- assumptions.

### From scratch

Calculate a simple t-statistic manually and/or with NumPy.

### Project ideas

- compare returns/price changes between two market regimes;
- compare operational metrics between two groups;
- A/B test analysis.

### Libraries

SciPy / statsmodels.

---

## 7.4 Chi-Square Tests + Cramer's V

### Learn

- categorical variables;
- contingency tables;
- observed vs expected frequencies;
- chi-square statistic;
- degrees of freedom;
- independence;
- goodness-of-fit vs independence tests;
- p-value interpretation;
- Cramer's V as effect size/association strength.

### From scratch

Build a small contingency table and manually calculate expected counts and the chi-square statistic.

### Project

Analyze relationships between categorical customer, operational, market-regime, or event variables.

---

## 7.5 ANOVA + Tukey HSD

### Learn

- why multiple t-tests are problematic;
- between-group vs within-group variance;
- F-statistic;
- one-way ANOVA;
- two-way ANOVA;
- interactions;
- assumptions;
- post-hoc testing;
- Tukey HSD.

### From scratch

Calculate a very small one-way ANOVA example to understand sums of squares and the F-statistic.

### Project

Compare a continuous outcome across multiple categories, market regimes, suppliers, locations, products, or operational groups.

---

## 7.6 Correlation and Association

### Topics

- covariance;
- Pearson correlation;
- Spearman correlation;
- monotonic vs linear relationships;
- correlation vs causation;
- significance testing;
- multicollinearity;
- categorical association measures;
- Theil's U as an optional revisit.

### Project

Feature relationship analysis on a pricing, market, operational, or business dataset.

---

## 7.7 Non-Parametric Tests

### Topics

- Mann-Whitney U;
- Wilcoxon signed-rank;
- Kruskal-Wallis;
- when parametric assumptions fail;
- ranks vs raw values.

### Goal

Understand alternatives rather than memorize every test.

---

# 8. Phase II - Regression and Predictive Modeling Foundations

## 8.1 Linear Regression

**Priority: Very High / Early Project**

### Learn

- supervised learning;
- regression problems;
- dependent vs independent variables;
- slope and intercept;
- coefficients;
- predictions;
- residuals;
- ordinary least squares;
- loss / squared error;
- assumptions;
- R-squared and adjusted R-squared;
- MAE;
- MSE;
- RMSE;
- multicollinearity;
- overfitting;
- train/test split.

### From scratch

Implement simple linear regression mathematically and/or using gradient descent with NumPy.

### Library implementation

scikit-learn and/or statsmodels.

### Project ideas

Prefer a dataset such as:

- commodity price relationships;
- energy demand/pricing;
- housing prices;
- operational forecasting;
- another continuous target dataset.

---

## 8.2 Multiple Linear Regression

### Learn

- multiple predictors;
- coefficient interpretation holding other variables constant;
- categorical encoding;
- interaction terms;
- multicollinearity;
- feature selection;
- residual diagnostics.

---

## 8.3 Polynomial Regression

### Learn

- nonlinear relationships represented through transformed features;
- polynomial features;
- overfitting;
- model complexity.

---

## 8.4 Regularization - Ridge / Lasso / Elastic Net

### Learn

- overfitting;
- coefficient penalties;
- L1 vs L2;
- feature shrinkage;
- Lasso feature selection;
- regularization strength;
- cross-validation.

---

## 8.5 Logistic Regression

**Priority: Very High**

### Learn

- binary classification;
- linear score;
- sigmoid function;
- probability output;
- odds and log-odds;
- coefficients;
- decision threshold;
- log loss / cross-entropy intuition;
- confusion matrix;
- accuracy;
- precision;
- recall;
- F1;
- ROC curve;
- ROC-AUC;
- class imbalance.

### From scratch

Implement the sigmoid and a simplified logistic regression training process.

### Project ideas

- customer churn;
- loan/default risk;
- direction-of-price-movement classification as an educational market example;
- equipment/process failure classification.

---

# 9. Phase III - Classical Machine Learning

## 9.1 K-Nearest Neighbors (KNN)

### Learn

- distance-based learning;
- Euclidean distance;
- K selection;
- feature scaling;
- classification/regression variants;
- curse of dimensionality.

### From scratch

Implement KNN manually with NumPy/Python.

---

## 9.2 Decision Trees

### Learn

- recursive splitting;
- Gini impurity;
- entropy/information gain;
- regression trees;
- depth;
- leaves;
- overfitting;
- pruning / constraints;
- feature importance.

### From scratch

Implement a simplified tree or manually work through several splits. Full production implementation is unnecessary.

---

## 9.3 Random Forest

### Learn

- ensembles;
- bagging;
- bootstrap samples;
- random feature subsets;
- variance reduction;
- out-of-bag intuition;
- feature importance;
- strengths and limitations.

### Project

Classification or regression dataset where performance can be compared with a single decision tree.

---

## 9.4 Gradient Boosting / XGBoost

### Learn

- boosting vs bagging;
- sequential error correction;
- weak learners;
- residual/error fitting intuition;
- learning rate;
- number of estimators;
- tree depth;
- regularization;
- overfitting;
- feature importance.

### From scratch

Do not implement production XGBoost from scratch. Use tiny conceptual/manual examples if useful.

### Project

Structured/tabular prediction problem, potentially financial, operational, or risk-related.

---

## 9.5 Support Vector Machines (SVM)

### Learn

- hyperplanes;
- margins;
- support vectors;
- soft margins;
- C;
- kernels;
- RBF kernel;
- gamma;
- scaling requirements.

### From scratch

Focus on geometric intuition rather than recreating the optimization solver.

---

## 9.6 Naive Bayes

### Learn

- Bayes' theorem;
- conditional probability;
- independence assumption;
- common variants;
- classification use cases.

---

# 10. Phase IV - Unsupervised Learning and Dimensionality Reduction

## 10.1 K-Means Clustering

### Learn

- unsupervised learning;
- centroids;
- assignment/update cycle;
- distance;
- scaling;
- initialization;
- inertia;
- elbow method;
- silhouette score;
- limitations.

### From scratch

Implement the assignment and centroid-update loop with NumPy.

### Project ideas

- customer segmentation;
- market-day clustering;
- asset/commodity behavior clustering;
- operational segmentation.

---

## 10.2 Hierarchical Clustering

### Learn

- agglomerative clustering;
- linkage;
- distance metrics;
- dendrograms;
- comparison with K-means.

---

## 10.3 DBSCAN

### Learn

- density-based clustering;
- epsilon;
- minimum samples;
- noise/outliers;
- irregular cluster shapes.

---

## 10.4 Principal Component Analysis (PCA)

### Learn

- dimensionality reduction;
- variance;
- covariance matrix;
- eigenvectors/eigenvalues intuition;
- principal components;
- explained variance;
- scaling;
- information loss;
- visualization.

### From scratch

Perform PCA on a small matrix using NumPy covariance/eigendecomposition before using sklearn.

### Project

Reduce a multi-feature dataset and analyze the resulting components.

---

# 11. Phase V - Model Evaluation and Data Science Judgment

These concepts should appear throughout earlier projects but eventually receive explicit focus.

## Topics

- train / validation / test sets;
- data leakage;
- cross-validation;
- stratification;
- feature engineering;
- preprocessing pipelines;
- missing values;
- categorical encoding;
- feature scaling;
- standardization vs normalization;
- class imbalance;
- oversampling/undersampling concepts;
- bias vs variance;
- underfitting vs overfitting;
- hyperparameters vs parameters;
- grid search;
- random search;
- model baselines;
- metric selection;
- calibration;
- interpretability;
- feature importance;
- SHAP concepts;
- reproducibility / random seeds.

## Capstone-style exercise

Only after individual models are familiar, use one dataset and compare several candidate models.

Harsh should be able to explain why each model was tried, how it was evaluated, and what tradeoffs exist.

---

# 12. Phase VI - Time Series and Forecasting

This phase begins connecting general data science to trading, commodities, markets, and risk.

## 12.1 Time-Series Foundations

### Topics

- time ordering;
- trend;
- seasonality;
- cycles;
- autocorrelation;
- lag features;
- rolling statistics;
- temporal train/test splits;
- leakage in time-series problems;
- stationarity.

### Projects

Use energy demand, commodity prices, power prices, stock prices, or other time-dependent data when appropriate.

---

## 12.2 Classical Forecasting

### Topics

- naive forecasts;
- moving averages;
- exponential smoothing;
- AR;
- MA;
- ARMA;
- ARIMA;
- differencing;
- ACF/PACF;
- forecast evaluation.

---

## 12.3 Volatility Modeling

### Topics

- returns;
- log returns;
- realized/rolling volatility;
- volatility clustering;
- ARCH/GARCH intuition and implementation.

This serves as a bridge toward quantitative finance/risk.

---

## 12.4 Regime Modeling

### Topics

- market regimes;
- Markov chains refresher;
- transition probabilities;
- Hidden Markov Models;
- regime classification/interpretation.

This should connect Harsh's prior stochastic-process coursework with practical market modeling.

---

# 13. Phase VII - Neural Networks and PyTorch

## 13.1 Neural Network Foundations

### Topics

- tensors;
- input features;
- weights;
- biases;
- linear transformations;
- hidden layers;
- activation functions;
- ReLU;
- sigmoid;
- softmax;
- logits;
- loss functions;
- MSE;
- binary cross-entropy;
- categorical cross-entropy;
- forward propagation;
- gradients;
- chain rule intuition;
- backpropagation;
- gradient descent;
- learning rate;
- epochs;
- batches;
- optimizers;
- overfitting;
- dropout;
- regularization;
- train/validation/test loops.

---

## 13.2 Project - Neural Network from Scratch

Use NumPy to build a small neural network.

Objective:

```text
inputs
 -> weighted sums
 -> activation
 -> output
 -> loss
 -> gradients
 -> weight updates
```

The goal is not production performance. The goal is to understand the machinery hidden by PyTorch.

---

## 13.3 Project - Rebuild with PyTorch

Recreate a similar problem using:

- `torch.Tensor`;
- `nn.Module`;
- `nn.Linear`;
- activation functions;
- loss functions;
- optimizers;
- `.backward()`;
- training loops;
- evaluation loops.

Explicitly compare what PyTorch automates against the from-scratch implementation.

---

## 13.4 Project - Real Neural Network Classification

Potential dataset: MNIST, Fashion-MNIST, or another manageable classification dataset.

Focus on:

- batching;
- epochs;
- validation;
- hyperparameters;
- learning curves;
- overfitting;
- regularization;
- performance interpretation.

---

# 14. Phase VIII - Applied Model Selection and Data Science Fluency

Only begin this phase once a meaningful portion of Phases I-VII has been completed.

## Goal

Transition from:

> "I know how to implement logistic regression."

into:

> "I recognize that this problem is a binary classification problem, know which models are reasonable, can build appropriate baselines, compare approaches, and defend my decision."

## Exercises

### Unknown Problem Exercises

Provide a dataset/problem without naming the required technique.

Harsh determines:

- problem type;
- target;
- feature types;
- preprocessing;
- statistical questions;
- candidate models/tests;
- metrics;
- validation strategy.

### Model Showdowns

Compare models such as:

- logistic regression vs decision tree vs random forest vs XGBoost;
- linear regression vs regularized regression vs tree-based regression;
- K-means vs hierarchical clustering vs DBSCAN where appropriate.

### Technical Defense

Harsh must defend choices verbally as if speaking to an interviewer, senior data scientist, or stakeholder.

---

# 15. Primary Track After Regression - AI / FDE / Agent Engineering

**This becomes the primary curriculum immediately after the current Regression module is completed.** The objective is to move from conceptual AI knowledge to independent implementation of AI systems and toward Forward Deployed Engineer-style problem solving.

The goal is not to abandon data science. Statistical inference, classification, tree models, time series, neural networks, and other DS/ML topics remain in this curriculum and should be revisited deliberately as a secondary track. They are no longer prerequisites for beginning AI engineering.

The AI/FDE track should emphasize building real systems: software structure, APIs, CLIs, data integration, LLM applications, retrieval, tools, agents, MCP, orchestration, evaluation, deployment, and eventually ambiguous customer-style problems.

## 15.1 LLM Application Foundations

### Topics

- APIs;
- HTTP basics as needed;
- requests/responses;
- authentication/environment variables;
- JSON;
- model inputs/outputs;
- system/developer/user instructions;
- structured outputs;
- context windows;
- tokenization;
- temperature/sampling concepts;
- error handling;
- retries;
- logging.

### Project

Build a small LLM-backed application directly through an API.

---

## 15.2 Tool / Function Calling

### Topics

- tool schemas;
- argument validation;
- model tool selection;
- executing application functions;
- returning tool results;
- error handling;
- deterministic workflows vs agentic behavior.

### Project

Build an assistant that selects among multiple real Python functions/tools.

Potential trading-oriented example: positions, exposures, prices, or risk-query tools.

---

## 15.3 Embeddings and Vector Databases

### Topics

- embeddings;
- vector representations;
- cosine similarity;
- nearest-neighbor search;
- indexing;
- metadata;
- vector databases;
- chunking.

### Project

Build semantic search over a document collection.

---

## 15.4 Retrieval-Augmented Generation (RAG)

### Topics

- ingestion;
- parsing;
- chunking;
- embedding;
- indexing;
- retrieval;
- top-k;
- context construction;
- generation;
- citations/grounding;
- retrieval evaluation;
- hallucination considerations.

### Project

Build a RAG system over technical, financial, or commodity documentation.

---

## 15.5 Agent Foundations

### Topics

- agent loop;
- model;
- instructions;
- tools;
- state;
- memory;
- stopping criteria;
- planning;
- execution;
- deterministic vs autonomous workflows;
- guardrails;
- evaluation.

### Project

Build a single agent with multiple tools and persistent state.

---

## 15.6 Memory and State

### Topics

- conversation state;
- short-term memory;
- long-term memory;
- semantic memory;
- episodic memory;
- databases/caches;
- vector memory;
- state machines;
- context management.

---

## 15.7 MCP

### Topics

- MCP architecture;
- clients;
- servers;
- tools;
- resources;
- prompts where relevant;
- discovery;
- transport;
- permissions/security;
- when MCP is useful vs direct integrations.

### Project

Build/use an MCP server exposing useful tools/resources to an AI application.

---

## 15.8 Multi-Agent Systems

### Topics

- single vs multi-agent systems;
- specialization;
- agent responsibilities;
- routing;
- handoffs;
- shared state;
- context isolation;
- orchestration;
- supervisor patterns;
- graph workflows;
- failure handling;
- observability;
- evaluation.

### Project

Build a multi-agent workflow with clearly separated responsibilities.

A commodities/risk research workflow would be a strong eventual application.

---

## 15.9 Production AI Engineering

### Topics

- FastAPI / service APIs;
- databases;
- asynchronous operations;
- queues where relevant;
- caching;
- testing;
- evaluations;
- observability;
- cost/latency;
- Docker;
- CI/CD;
- cloud deployment;
- Kubernetes where justified;
- security/permissions;
- human-in-the-loop systems.

### Capstone

Build a production-style AI application combining models, tools, data, storage, APIs, evaluation, and deployment.

---

# 16. Phase X - Quantitative Finance, Trading, and Risk (Future Major Track)

This track can develop alongside later AI engineering work. It is not the primary immediate objective, but market-oriented datasets should be used earlier whenever they naturally support the statistical concept being learned.

## Foundations

- prices vs returns;
- simple vs log returns;
- expected return;
- variance/volatility;
- covariance/correlation;
- drawdowns;
- compounding;
- market data structure;
- liquidity;
- bid/ask spreads;
- exposure;
- P&L.

## Risk Analytics

- Value at Risk (VaR);
- historical VaR;
- parametric VaR;
- Monte Carlo VaR;
- Expected Shortfall / CVaR;
- stress testing;
- scenario analysis;
- sensitivities;
- portfolio risk;
- diversification;
- correlation risk.

## Derivatives

- forwards;
- futures;
- options;
- swaps;
- calls/puts;
- payoff diagrams;
- intrinsic/time value;
- Greeks;
- hedging;
- Black-Scholes intuition;
- implied volatility.

## Portfolio / Asset Modeling

- portfolio return;
- portfolio variance;
- covariance matrices;
- diversification;
- efficient frontier;
- Sharpe ratio;
- optimization;
- factor models.

## Commodity / Energy Topics

- futures curves;
- contango/backwardation;
- basis;
- location spreads;
- calendar spreads;
- crack spreads;
- storage economics;
- pipeline/transport constraints;
- power pricing;
- weather effects;
- physical vs financial exposure;
- hedging commodity exposure.

## Quantitative Projects

Potential future projects include:

- calculate and visualize stock/commodity returns;
- build a rolling-volatility dashboard;
- calculate historical/parametric/Monte Carlo VaR;
- stress-test a portfolio;
- model correlated assets;
- construct an efficient frontier;
- price simple options;
- simulate option payoffs;
- forecast commodity demand/prices;
- analyze commodity spreads;
- detect market regimes with Markov/HMM methods;
- build a risk analytics API;
- combine quantitative analytics with an AI agent interface.

---

# 17. Supporting Software Engineering Skills

These should mostly be learned organically while building projects rather than as prerequisites.

## Python Fluency

Strengthen through repeated use:

- functions;
- loops/comprehensions;
- dictionaries/sets/lists;
- error handling;
- modules;
- package structure;
- virtual environments;
- typing where useful;
- debugging.

## NumPy

Reinforce through from-scratch ML work:

- arrays;
- dimensions/shapes;
- indexing;
- broadcasting;
- vectorization;
- matrix multiplication;
- aggregation;
- random generation;
- linear algebra.

## OOP

Reinforce naturally through model and AI projects:

- classes;
- instances;
- constructors;
- attributes;
- methods;
- inheritance;
- composition;
- encapsulation;
- polymorphism;
- when OOP is actually useful.

## Visualization

Reinforce throughout projects:

- Matplotlib;
- Plotly where useful;
- distributions;
- scatter plots;
- residual plots;
- confusion matrices;
- ROC curves;
- feature importance;
- time-series charts;
- communicating results rather than merely making charts.

## Git / GitHub

Use the curriculum repository to practice:

- repositories;
- commits;
- branches when useful;
- README files;
- `.gitignore`;
- requirements/environment management;
- clean project history;
- documentation.

## Deployment (Later)

Revisit as projects become applications:

- APIs;
- Docker;
- images/containers;
- CI/CD;
- cloud deployment;
- Kubernetes;
- monitoring/logging.

---

# 18. Recommended Repository Structure

Suggested repository name:

```text
applied-ml-lab
```

Initial structure:

```text
applied-ml-lab/
│
├── README.md
├── CURRICULUM.md
├── requirements.txt
│
├── 01-descriptive-statistics/
│   ├── README.md
│   ├── notes.md
│   ├── notebook.ipynb
│   └── data/
│
├── 02-t-tests/
├── 03-chi-square/
├── 04-anova/
├── 05-linear-regression/
├── 06-logistic-regression/
├── 07-knn/
├── 08-decision-trees/
├── 09-random-forest/
├── 10-xgboost/
├── 11-svm/
├── 12-kmeans/
├── 13-pca/
├── 14-time-series/
├── 15-neural-network-numpy/
├── 16-neural-network-pytorch/
└── ...
```

The exact order can change as the curriculum evolves.

## Each project folder should eventually contain

### `README.md`

A polished, concise explanation suitable for GitHub:

- problem;
- dataset;
- technique;
- why the technique was used;
- approach;
- results;
- interpretation;
- key takeaways.

### `notes.md`

Personal knowledge base:

- What is this technique?
- How does it work?
- Important formulas.
- Assumptions.
- Preprocessing requirements.
- How to interpret outputs.
- Common mistakes.
- What confused me?
- What did I learn?
- What do I want to remember six months from now?

### `notebook.ipynb`

Actual analysis and implementation.

### `data/`

Dataset or instructions/source for retrieving it. Avoid committing large or restricted datasets directly when inappropriate.

---

# 19. Dataset Philosophy

Whenever possible, choose datasets that reinforce multiple interests without compromising the primary learning objective.

Preferred domains include:

- commodities;
- energy;
- power;
- crude oil;
- natural gas;
- equities;
- financial markets;
- risk;
- operations;
- manufacturing;
- supply chains;
- real-world business data.

However, **do not force a finance dataset onto a technique when a cleaner educational dataset would teach the technique substantially better**.

The statistical/ML concept remains the primary objective during the early phases.

---

# 20. Future Knowledge Base / Obsidian / Knowledge Graph

Do not prioritize building this now.

First create useful knowledge through projects.

Once enough project notes exist, the repository can become the source material for a personal technical knowledge system.

Potential future structure could connect concepts such as:

```text
Linear Regression
    -> Residuals
    -> MSE
    -> Gradient Descent
    -> Regularization
    -> Neural Networks

Logistic Regression
    -> Sigmoid
    -> Probability
    -> Log Loss
    -> Classification
    -> Neural Networks

PCA
    -> Variance
    -> Covariance Matrix
    -> Eigenvectors
    -> Dimensionality Reduction

Chi-Square
    -> Categorical Variables
    -> Contingency Tables
    -> Cramer's V

Time Series
    -> Autocorrelation
    -> ARIMA
    -> Volatility
    -> GARCH
    -> Market Regimes
```

Possible future tools include:

- Obsidian;
- Markdown backlinks;
- knowledge graphs;
- embeddings/vector search;
- RAG over Harsh's own notes;
- an AI tutor that retrieves prior projects and quizzes Harsh.

Building that system could itself become a future AI-engineering project.

---

# 21. Current Priority Sequence and Two-Track Plan

The curriculum is deliberately flexible. There is **no fixed projects-per-week requirement**, and the entire data-science roadmap does **not** need to be completed before beginning AI engineering.

## Immediate Transition Point

The current priority is to **finish the Regression module well**, including the current natural-gas project and the important regression concepts already in progress:

1. feature engineering;
2. lagged variables;
3. seasonality;
4. Ridge / Lasso regularization;
5. regression diagnostics and evaluation;
6. final interpretation / write-up;
7. regression recall / technical defense.

Once this is complete:

> **Pause the sequential Data Science curriculum and make AI / FDE Engineering the primary track.**

## Primary Track - AI / Software / FDE Engineering

A sensible progression is:

1. Python/software-engineering reinforcement through real builds
2. application structure, modules, OOP, typing, exceptions, and testing
3. HTTP and APIs
4. FastAPI / backend services
5. CLI development
6. LLM APIs and structured outputs
7. tool / function calling
8. embeddings and vector databases
9. RAG
10. retrieval evaluation and AI evals
11. single-agent systems
12. state, context, and memory
13. MCP clients / servers / tools / resources
14. orchestration and multi-agent systems
15. Docker, deployment, observability, security, and production concerns
16. FDE-style projects with ambiguous requirements, multiple data sources, and end-to-end system ownership

The emphasis should remain:

> **Understand -> Implement -> Build -> Debug -> Explain -> Rebuild independently**

Do not spend months on AI theory before building. Each major concept should quickly lead to an implementation or project.

## Secondary Track - Data Science / Statistics / ML

Data science remains important and should be revisited throughout the AI/FDE track rather than abandoned.

### High-Priority Prior-Work / Tesla Toolkit

These topics deserve deliberate refresh/build sessions because they overlap directly with prior professional analytics work:

1. t-tests / Welch's t-test + Cohen's d
2. F-statistic / one-way and two-way ANOVA
3. Tukey HSD
4. chi-square tests + Cramer's V
5. logistic regression
6. classification metrics and thresholds
7. decision trees
8. random forests
9. gradient boosting / XGBoost introduction

These do **not** need to be completed before starting AI engineering.

A useful pattern is to interleave them between AI projects:

```text
Finish Regression
    ->
AI / backend project
    ->
t-test + ANOVA refresh/build
    ->
RAG project
    ->
logistic regression / classification refresh
    ->
Agent project
    ->
decision tree / random forest refresh
    ->
MCP / FDE project
```

This creates spaced repetition while keeping the main curriculum aligned with the AI/FDE objective.

### Later / Return-When-Useful DS Topics

The following remain in scope but are not immediate prerequisites:

- KNN;
- SVM;
- clustering;
- PCA;
- deeper time-series forecasting;
- volatility modeling;
- regime modeling;
- neural networks / PyTorch;
- broader model-selection exercises;
- advanced quantitative finance/risk modeling.

Return to these when they become relevant to a project, interview, role, or specific learning objective.

## Guiding Scheduling Rule

Do not optimize for completing the curriculum in textbook order.

Optimize for:

1. closing the current Regression module properly;
2. building independent software and AI engineering depth;
3. retaining the statistical/ML toolkit through deliberate interleaving;
4. selecting later DS topics based on practical relevance.

---

# 22. Example: What a Successful Linear Regression Module Looks Like

This serves as the template for how early modules should operate.

## Refresh

Harsh can explain:

- regression vs classification;
- target vs features;
- line/plane of best fit;
- coefficients/intercept;
- predictions;
- residuals;
- ordinary least squares;
- MSE/RMSE/MAE;
- R-squared;
- assumptions;
- train/test split;
- common preprocessing issues.

## Mechanics

Harsh manually works through a tiny regression example and/or implements a simplified regression process with NumPy.

## Project

Harsh receives a dataset and is explicitly told to build a linear regression analysis/model.

Harsh independently:

1. loads the data;
2. inspects it;
3. cleans/prepares relevant columns;
4. performs useful EDA;
5. defines X and y;
6. creates a train/test split;
7. fits the model;
8. generates predictions;
9. calculates appropriate metrics;
10. visualizes relevant results/residuals;
11. interprets coefficients and model performance.

## Documentation

Harsh writes the README and personal notes largely in his own words.

## Interview

Potential questions:

- Explain linear regression.
- What is OLS minimizing?
- What is a residual?
- What does a coefficient mean?
- What is R-squared?
- R-squared vs RMSE?
- Why split training and testing data?
- What assumptions does linear regression make?
- What is multicollinearity?
- How would outliers affect the model?
- What would you do if the relationship were nonlinear?
- Write a basic sklearn linear regression workflow from memory.

## Delayed Recall

Revisit these questions and implementation later without reopening the completed project first.

---

# 23. Guiding Principle

This curriculum should continuously move Harsh through the following progression:

```text
I've heard of it
        ↓
I understand the explanation
        ↓
I understand the mechanics
        ↓
I can implement it with guidance
        ↓
I can implement it independently
        ↓
I can interpret and debug it
        ↓
I can explain it under pressure
        ↓
I remember it weeks later
        ↓
I know when to use it
        ↓
I can compare it against alternatives
        ↓
I can teach and defend it
```

The curriculum succeeds when Harsh no longer needs an LLM to substitute for technical knowledge. AI can remain a useful accelerator, reviewer, documentation aid, and collaborator—but the underlying expertise should belong to Harsh.

---

# 24. Next Action

## Current

Complete the **Regression module** and the current natural-gas regression project.

The remaining immediate work is:

1. apply feature engineering, lagged variables, and seasonality;
2. learn/apply Ridge and Lasso;
3. complete regression diagnostics and evaluation;
4. interpret and document the final model;
5. complete a short regression recall / technical-defense check.

## Then Pivot

After Regression:

> **AI / FDE Engineering becomes the primary track.**

Begin with software/application foundations and quickly progress into APIs, FastAPI, CLI development, LLM APIs, tool calling, embeddings/vector databases, RAG, agents, MCP, orchestration, production engineering, and FDE-style end-to-end projects.

Do **not** require completion of classification, trees, clustering, time series, neural networks, or the rest of the traditional data-science sequence before this pivot.

## Continue Data Science in Parallel

Periodically return to the high-priority statistical/ML toolkit—especially t-tests, ANOVA/F-tests, Tukey HSD, chi-square/Cramer's V, logistic regression, decision trees, random forests, and boosting—between AI projects.

The curriculum is therefore no longer a single linear sequence. It becomes:

```text
                    PRIMARY
Finish Regression -> AI / Software / FDE Engineering
                          |
                          | interleave / revisit
                          v
                    SECONDARY
              Statistics / DS / ML
```

Update this document as projects are completed and as career priorities evolve.
