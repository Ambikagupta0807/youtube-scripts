# YouTube Script Generator

An AI pipeline that takes a raw topic and produces a complete, ready-to-record YouTube
video script for a technical education channel — built entirely on Google Gemini's
free tier.

## What it does

1. Generates 10 candidate video titles for a given topic, optimized for a 10-minute
   video format
2. Evaluates all 10 titles against CTR-focused criteria (hook strength, mobile
   readability, actionable outcome) and selects the single best one
3. Writes a full ~1500-word, timestamped script — hook, core teaching broken into
   named beats, common mistakes, and a recap — following a structured format
   designed for spoken narration, not prose
4. Scores the generated script against 11 criteria (clarity, accuracy, engagement,
   coverage, etc.) with a reviewer-style rating out of 10 for each

## Why this project

Each stage uses a distinct, carefully scoped system prompt — the title generator,
title selector, scriptwriter, and script reviewer are deliberately separate calls
with separate responsibilities, rather than one long prompt trying to do everything.
This keeps each step's output focused and makes the pipeline easy to debug stage by stage.

## Tech stack

Python · Google Gemini API · python-dotenv

## Key features

- Multi-stage LLM pipeline (generate → select → write → evaluate)
- CTR-focused title selection with explicit, structured criteria
- Structured script format with scene direction cues for recording
- Automated script quality scoring across 11 educational-content criteria
- Runs entirely on Gemini's free tier — no paid API required
