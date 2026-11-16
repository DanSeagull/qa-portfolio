# QA Automation MCP Server (Python)

A **Model Context Protocol (MCP) server** in Python that connects an LLM (Claude) with QA tooling, a **test management system (Allure TestOps)** and **GitHub**, so test artifacts can be created and maintained straight from the assistant.

## What it does

Exposes MCP tools that let the assistant:

- create and update **test cases**
- build and edit **checklists**
- create **test plans**
- link these artifacts to GitHub

It turns natural-language requests into real test management changes without manual click-work.

## Stack

`Python` · `MCP (Model Context Protocol)` · test management system API · GitHub API

## Why it matters

- Removes repetitive manual work in the test management UI.
- Keeps test cases and plans consistent and close to code and CI.
- Shows building on the MCP standard to integrate an LLM with real engineering systems: authentication, API clients, tool schemas.

## My role

Designed and implemented the server end to end: the tool surface (test cases, checklists, test plans) and the integrations with the test management system, GitHub and the assistant.
