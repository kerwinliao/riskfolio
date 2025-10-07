<img src="logo.png" alt="riskfolio Logo">

# riskfolio

**riskfolio** is a Python library for capital attribution, RWA (Risk-Weighted Assets) analysis, and profitability evaluation in financial risk management. It provides a modular and object-oriented framework to calculate, attribute, and visualize key risk metrics such as TCE (Tangible Common Equity) allocation, capital charge, return on capital, and RWA share.  

The library is designed for quant developers, risk managers, and financial analysts who want a flexible and extensible way to model portfolio risk and performance attribution at various aggregation levels (e.g., desk, product, portfolio).

This library is still in beta version. Please read instructions carefully before using and check the details of each function when necessary.

---

## 📘 Overview: Risk Attribution for Modern Banking Portfolios

In the post-Basel III era, capital allocation is no longer a matter of simple portfolio optimization — it is a regulatory imperative. Banks are required to calculate and manage a series of risk-sensitive metrics such as Risk-Weighted Assets (RWA), Total Common Equity (TCE) allocation, and G-SIB (Global Systemically Important Bank) scores. These measures directly influence a bank’s minimum capital requirements, cost of equity, and even its systemic surcharge, shaping everything from product pricing to strategic asset mix.

This project provides a modular, Python-based library that demonstrates how these regulatory metrics can be computed, attributed, and stress-tested at a granular level (e.g., by desk, product, or counterparty). Built around synthetic fixed-income trading data, it illustrates the computational backbone behind modern regulatory reporting and internal capital allocation — serving as both a teaching tool and a foundation for production-scale systems.

---

## ⚖️ From Mean-Variance Allocation to Basel-Aligned Attribution


 Traditional portfolio asset allocation techniques focus on optimizing risk-adjusted returns by balancing expected return, volatility, and correlation — often ignoring regulatory constraints. However, for banks subject to Basel III, capital is the scarce resource, and decisions must be evaluated through the lens of their regulatory cost. For example, a high-yield bond desk might offer attractive returns, but its elevated RWA and G-SIB contribution could erode net profitability once capital charges are considered.

This library bridges that gap. Instead of optimizing portfolios purely for Sharpe ratios or tracking error, it enables users to attribute capital consumption and regulatory costs across organizational dimensions. The result is a clear picture of which activities truly create economic value after accounting for regulatory drag, and how alternative risk-weight or business-mix scenarios would impact capital efficiency.

---

## 🚀 Features

- **Capital Charge Computation** – Calculate capital charge and net income from allocated TCE and PnL.  
- **Attribution Table Generation** – Aggregate key metrics by desk, product, or other dimensions with automatically calculated performance ratios.  
- **Scenario Analysis** – Apply weight changes to products and instantly recompute RWA and profitability metrics.  
- **Extensible Design** – Built with modular components (`core`, `reporting`, `validators`, `exceptions`, etc.) to support future extensions.  
- **Object-Oriented API** – Easily integrate with larger analytics pipelines or use as a standalone analysis tool.  

---

## 🧰 Core Functions & Usage Guide



---

## 📊 Mock Data & Result Demonstration



---

## 📦 Installation

Clone the repository and install the package in **editable mode** (recommended during development):

```bash
pip install riskfolio-beta
