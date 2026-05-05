#!/usr/bin/env python3
"""Generate usermodel.html — full rebuild with correct CSS + rich Django content."""
import pathlib

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Django User Model Masterclass &mdash; code::core</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,400&family=Jost:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style>
    :root {
      --navy:      #0D2340;
      --navy-dark: #0D2340;
      --blue-800:  #14305A;
      --blue-700:  #1E4D8C;
      --blue-500:  #3970B8;
      --blue-300:  #7AAAD6;
      --blue-50:   #EAF0FA;
      --gold:      #B8922A;
      --ivory:     #F9F6EF;
      --ink:       #1C1A16;
      --ink-mid:   #3D3A32;
      --ink-soft:  #6B6760;
      --rule:      #D5CFC3;
      --parch:     #EDE8DC;
      --green:     #2A6B43;
      --green-bg:  #EAF3EE;
      --amber:     #9A5B0A;
      --amber-bg:  #FDF3E3;
      --red:       #8C2020;
      --red-bg:    #FAEAEA;
      --info-bg:   #EAF0FA;
      --r:  10px;
      --rs: 6px;
      --rl: 16px;
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      background: var(--ivory);
      color: var(--ink);
      font-family: 'Jost', sans-serif;
      font-size: 15px;
      font-weight: 300;
      line-height: 1.85;
    }
    ::selection { background: var(--navy); color: var(--ivory); }
    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-track { background: var(--ivory); }
    ::-webkit-scrollbar-thumb { background: var(--rule); border-radius: 3px; }

    .wrapper { display: flex; min-height: 100vh; }

    .sidebar {
      width: 280px; min-width: 280px;
      background: var(--navy);
      padding: 0;
      position: sticky; top: 0;
      height: 100vh; overflow-y: auto;
      display: flex; flex-direction: column;
    }
    .sidebar::-webkit-scrollbar-track { background: var(--navy); }
    .sidebar::-webkit-scrollbar-thumb { background: var(--blue-700); }
    .sidebar-brand {
      padding: 2rem 1.75rem 1.5rem;
      border-bottom: 1px solid rgba(255,255,255,.1);
    }
    .brand-wordmark {
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px; font-weight: 700;
      letter-spacing: .08em; color: var(--ivory);
      margin-bottom: .25rem;
    }
    .brand-wordmark span { color: var(--gold); }
    .brand-sub {
      font-family: 'Jost', sans-serif;
      font-size: 11px; font-weight: 600;
      letter-spacing: .15em; text-transform: uppercase;
      color: var(--blue-300);
    }
    .nav-group { padding: 1.25rem 1.75rem .5rem; }
    .nav-group-label {
      font-size: 10px; font-weight: 600;
      letter-spacing: .15em; text-transform: uppercase;
      color: var(--blue-300); margin-bottom: .6rem; opacity: .7;
    }
    .nav-link {
      display: flex; align-items: center; gap: .6rem;
      padding: .45rem .65rem; border-radius: var(--rs);
      color: rgba(255,255,255,.65); text-decoration: none;
      font-size: 13px; font-weight: 400; transition: all .15s;
      margin-bottom: 2px;
    }
    .nav-link:hover { background: rgba(255,255,255,.08); color: var(--ivory); }
    .nav-link.active { background: var(--gold); color: var(--navy); font-weight: 600; }
    .nav-num {
      width: 18px; height: 18px; min-width: 18px;
      border-radius: 50%; background: rgba(255,255,255,.1);
      font-family: 'JetBrains Mono', monospace;
      font-size: 9px; font-weight: 700;
      display: flex; align-items: center; justify-content: center;
      color: rgba(255,255,255,.5);
    }
    .nav-link.active .nav-num { background: rgba(13,35,64,.2); color: var(--navy); }
    .sidebar-footer {
      margin-top: auto; padding: 1.25rem 1.75rem;
      border-top: 1px solid rgba(255,255,255,.08);
      font-size: 11px; color: rgba(255,255,255,.3);
      font-family: 'JetBrains Mono', monospace;
    }

    .main { flex: 1; min-width: 0; padding: 3.5rem 5rem 5rem; max-width: 900px; }

    .hero {
      background: var(--navy); border-radius: var(--rl);
      padding: 3.5rem; margin-bottom: 4rem;
      position: relative; overflow: hidden;
    }
    .hero::before {
      content: ""; position: absolute;
      top: -60px; right: -60px; width: 300px; height: 300px;
      background: radial-gradient(circle, rgba(184,146,42,.25) 0%, transparent 70%);
      pointer-events: none;
    }
    .hero::after {
      content: ""; position: absolute;
      bottom: -40px; left: -40px; width: 200px; height: 200px;
      background: radial-gradient(circle, rgba(30,77,140,.4) 0%, transparent 70%);
      pointer-events: none;
    }
    .hero-eyebrow {
      font-size: 11px; font-weight: 600;
      letter-spacing: .15em; text-transform: uppercase;
      color: var(--gold); margin-bottom: 1rem;
    }
    .hero h1 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 52px; font-weight: 600; line-height: 1.05;
      color: var(--ivory); margin-bottom: 1.25rem;
    }
    .hero h1 em { font-style: italic; color: var(--gold); }
    .hero-desc {
      font-size: 15px; font-weight: 300; line-height: 1.85;
      color: rgba(249,246,239,.7); max-width: 540px;
    }
    .hero-stats {
      display: flex; gap: 0; margin-top: 2.5rem;
      padding-top: 2rem; border-top: 1px solid rgba(255,255,255,.12);
    }
    .hero-stat {
      flex: 1; padding-right: 2rem;
      border-right: 1px solid rgba(255,255,255,.1); margin-right: 2rem;
    }
    .hero-stat:last-child { border-right: none; margin-right: 0; padding-right: 0; }
    .stat-val {
      font-family: 'Cormorant Garamond', serif;
      font-size: 26px; font-weight: 600; color: var(--gold);
      line-height: 1; margin-bottom: .2rem;
    }
    .stat-label {
      font-size: 11px; font-weight: 600;
      letter-spacing: .1em; text-transform: uppercase;
      color: rgba(249,246,239,.4);
    }

    .section { margin-bottom: 4rem; scroll-margin-top: 2rem; }
    .section-header {
      display: flex; align-items: flex-start; gap: 1.25rem;
      margin-bottom: 2rem; padding-bottom: 1.5rem;
      border-bottom: 2px solid var(--parch);
    }
    .section-num-badge {
      width: 40px; height: 40px; min-width: 40px;
      background: var(--navy); color: var(--ivory);
      border-radius: var(--rs);
      display: flex; align-items: center; justify-content: center;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px; font-weight: 700; margin-top: 3px;
    }
    .section-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: 28px; font-weight: 600; color: var(--navy); line-height: 1.1;
    }
    .section-subtitle {
      font-size: 13px; font-weight: 400; color: var(--ink-soft); margin-top: .2rem;
    }

    .concept {
      background: var(--blue-50);
      border: 1px solid var(--blue-300);
      border-left: 4px solid var(--blue-700);
      border-radius: var(--r); padding: 1.5rem 1.75rem; margin: 1.5rem 0;
    }
    .concept-label {
      font-size: 10px; font-weight: 600;
      letter-spacing: .15em; text-transform: uppercase;
      color: var(--blue-700); margin-bottom: .6rem;
    }
    .concept h3 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 20px; font-weight: 600; color: var(--navy); margin-bottom: .5rem;
    }
    .concept p { font-size: 14px; color: var(--ink-mid); line-height: 1.85; margin-bottom: .5rem; }
    .concept p:last-child { margin-bottom: 0; }

    .analogy {
      background: var(--parch);
      border: 1px solid var(--rule); border-left: 4px solid var(--gold);
      border-radius: var(--r); padding: 1.25rem 1.5rem; margin: 1.25rem 0;
    }
    .analogy-label {
      font-size: 10px; font-weight: 600;
      letter-spacing: .15em; text-transform: uppercase;
      color: var(--gold); margin-bottom: .4rem;
    }
    .analogy p { font-size: 14px; font-style: italic; color: var(--ink-mid); line-height: 1.8; margin: 0; }

    .callout {
      display: flex; gap: 1rem; padding: 1.1rem 1.4rem;
      border-radius: var(--r); margin: 1.25rem 0; border-left: 4px solid;
    }
    .callout-info    { background: var(--info-bg);  border-color: var(--blue-500); }
    .callout-warn    { background: var(--amber-bg); border-color: var(--amber);    }
    .callout-success { background: var(--green-bg); border-color: var(--green);    }
    .callout-danger  { background: var(--red-bg);   border-color: var(--red);      }
    .callout-icon { font-size: 16px; min-width: 20px; margin-top: 2px; }
    .callout-tag {
      font-size: 9px; font-weight: 700;
      letter-spacing: .15em; text-transform: uppercase; margin-bottom: .2rem;
    }
    .callout-info    .callout-tag { color: var(--blue-700); }
    .callout-warn    .callout-tag { color: var(--amber);    }
    .callout-success .callout-tag { color: var(--green);    }
    .callout-danger  .callout-tag { color: var(--red);      }
    .callout p { font-size: 14px; color: var(--ink-mid); line-height: 1.75; margin: 0; }
    .callout strong { color: var(--ink); font-weight: 600; }

    .code-block {
      background: var(--navy); border-radius: var(--r);
      overflow: hidden; margin: 1.5rem 0;
      box-shadow: 0 4px 24px rgba(13,35,64,.12);
    }
    .code-top {
      display: flex; align-items: center; justify-content: space-between;
      padding: .65rem 1.25rem; background: var(--blue-800);
      border-bottom: 1px solid rgba(255,255,255,.08);
    }
    .code-file {
      display: flex; align-items: center; gap: .5rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px; font-weight: 500; color: var(--blue-300);
    }
    .code-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--gold); }
    .code-badge {
      font-size: 9px; font-weight: 700;
      letter-spacing: .12em; text-transform: uppercase;
      background: rgba(255,255,255,.06); color: rgba(255,255,255,.35);
      padding: .2rem .55rem; border-radius: 999px;
    }
    pre {
      padding: 1.5rem 1.75rem; overflow-x: auto;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px; font-weight: 400; line-height: 1.75; color: #C9D1D9;
    }
    code { font-family: inherit; }
    .k { color: #D2A8FF; }
    .s { color: #A5D6A7; }
    .c { color: #6B6760; font-style: italic; }
    .v { color: #79C0FF; }
    .n { color: #F0A868; }
    .f { color: var(--gold); }
    .o { color: #FF7B72; }
    :not(pre) > code {
      background: var(--parch); border: 1px solid var(--rule);
      color: var(--blue-700); padding: .12em .4em; border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12.5px; font-weight: 500;
    }

    .annotated-code { display: flex; flex-direction: column; }
    .ann-line { display: flex; gap: 1.5rem; margin: .5rem 0; align-items: flex-start; }
    .ann-code {
      font-family: 'JetBrains Mono', monospace; font-size: 12.5px;
      background: var(--navy); color: #C9D1D9;
      padding: .5rem .9rem; border-radius: var(--rs);
      min-width: 280px; line-height: 1.6;
    }
    .ann-text { font-size: 13.5px; color: var(--ink-mid); padding-top: .4rem; line-height: 1.65; flex: 1; }
    .ann-text strong { color: var(--navy); font-weight: 600; }

    .step-list { display: flex; flex-direction: column; gap: .85rem; }
    .step-card {
      display: flex; gap: 1.25rem; background: #fff;
      border: 1px solid var(--rule); border-radius: var(--r);
      padding: 1.25rem 1.5rem; transition: box-shadow .15s;
    }
    .step-card:hover { box-shadow: 0 4px 16px rgba(13,35,64,.07); }
    .step-circle {
      width: 32px; height: 32px; min-width: 32px;
      border-radius: 50%; background: var(--navy); color: var(--ivory);
      font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700;
      display: flex; align-items: center; justify-content: center; margin-top: 2px;
    }
    .step-card.gold .step-circle { background: var(--gold); }
    .step-card.blue .step-circle { background: var(--blue-700); }
    .step-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: 18px; font-weight: 600; color: var(--navy); margin-bottom: .3rem;
    }
    .step-desc { font-size: 14px; color: var(--ink-soft); line-height: 1.75; margin-bottom: .75rem; }
    .step-desc:last-child { margin-bottom: 0; }
    .step-why {
      font-size: 13px; color: var(--blue-700); background: var(--blue-50);
      border-radius: var(--rs); padding: .6rem .9rem; line-height: 1.65;
    }
    .step-why strong { font-weight: 600; }

    .compare { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.5rem 0; }
    .compare-card { border-radius: var(--r); padding: 1.5rem; border: 1px solid; }
    .compare-card.bad  { background: var(--red-bg);   border-color: #E8B4B4; }
    .compare-card.good { background: var(--green-bg); border-color: #B4D6C0; }
    .compare-label {
      font-size: 10px; font-weight: 700;
      letter-spacing: .15em; text-transform: uppercase; margin-bottom: .6rem;
    }
    .compare-card.bad  .compare-label { color: var(--red);   }
    .compare-card.good .compare-label { color: var(--green); }
    .compare-card h4 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 17px; font-weight: 600; margin-bottom: .4rem;
    }
    .compare-card.bad  h4 { color: var(--red);   }
    .compare-card.good h4 { color: var(--green); }
    .compare-card p { font-size: 13.5px; color: var(--ink-mid); line-height: 1.7; margin: 0; }

    .card-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.5rem 0; }
    .card { background: #fff; border: 1px solid var(--rule); border-radius: var(--r); padding: 1.5rem; }
    .card-icon { font-size: 22px; margin-bottom: .75rem; }
    .card h4 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 18px; font-weight: 600; color: var(--navy); margin-bottom: .4rem;
    }
    .card p { font-size: 13.5px; color: var(--ink-soft); line-height: 1.75; margin: 0; }

    .table-wrap { overflow-x: auto; margin: 1.5rem 0; border-radius: var(--r); border: 1px solid var(--rule); }
    table { width: 100%; border-collapse: collapse; font-size: 13.5px; }
    thead { background: var(--navy); }
    th {
      color: rgba(249,246,239,.7);
      font-size: 10px; font-weight: 600;
      letter-spacing: .12em; text-transform: uppercase;
      padding: .85rem 1.25rem; text-align: left;
    }
    td {
      padding: .85rem 1.25rem; border-bottom: 1px solid var(--parch);
      color: var(--ink-mid); vertical-align: top; line-height: 1.6;
    }
    tr:last-child td { border-bottom: none; }
    tr:nth-child(even) td { background: rgba(237,232,220,.25); }
    td strong { color: var(--ink); font-weight: 600; }

    .badge {
      display: inline-flex; align-items: center;
      padding: .2rem .6rem; border-radius: 999px;
      font-size: 10px; font-weight: 700; letter-spacing: .08em;
    }
    .badge-navy   { background: var(--navy);     color: var(--ivory); }
    .badge-gold   { background: var(--gold);     color: #fff; }
    .badge-green  { background: var(--green-bg); color: var(--green); border: 1px solid #B4D6C0; }
    .badge-blue   { background: var(--blue-50);  color: var(--blue-700); border: 1px solid var(--blue-300); }
    .badge-amber  { background: var(--amber-bg); color: var(--amber); border: 1px solid #F2CDA0; }
    .badge-red    { background: var(--red-bg);   color: var(--red);   border: 1px solid #E8B4B4; }

    .rule { border: none; border-top: 2px solid var(--parch); margin: 3rem 0; }

    p { color: var(--ink-mid); margin-bottom: .9rem; line-height: 1.85; }
    p:last-child { margin-bottom: 0; }
    h2 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 22px; font-weight: 600; color: var(--navy); margin: 2rem 0 .75rem;
    }
    h3 {
      font-family: 'Jost', sans-serif;
      font-size: 11px; font-weight: 600;
      letter-spacing: .15em; text-transform: uppercase;
      color: var(--ink-soft); margin: 1.5rem 0 .6rem;
    }
    ul, ol { padding-left: 1.5rem; color: var(--ink-soft); font-size: 14px; line-height: 1.8; }
    li { margin-bottom: .4rem; }

    .footer {
      margin-top: 5rem; padding: 2rem 0 1rem;
      border-top: 2px solid var(--parch);
      display: flex; align-items: center; justify-content: space-between;
      flex-wrap: wrap; gap: 1rem;
    }
    .footer-brand {
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px; font-weight: 700; color: var(--navy);
    }
    .footer-brand span { color: var(--gold); }
    .footer p { font-size: 12px; color: var(--ink-soft); margin: 0; }

    @media (max-width: 960px) {
      .sidebar { display: none; }
      .main { padding: 2rem 1.5rem; }
      .card-grid, .compare { grid-template-columns: 1fr; }
      .hero { padding: 2.5rem 2rem; }
      .hero h1 { font-size: 38px; }
      .ann-line { flex-direction: column; gap: .5rem; }
      .ann-code { min-width: unset; }
    }
  </style>
</head>
<body>
<div class="wrapper">

  <!-- SIDEBAR -->
  <nav class="sidebar">
    <div class="sidebar-brand">
      <div class="brand-wordmark">code<span>::</span>core</div>
      <div class="brand-sub">User Model Masterclass</div>
    </div>

    <div class="nav-group">
      <div class="nav-group-label">Foundations</div>
      <a href="#mental-model"  class="nav-link active"><span class="nav-num">01</span> Mental Model</a>
      <a href="#builtin-user"  class="nav-link"><span class="nav-num">02</span> Built-in User</a>
      <a href="#strategies"    class="nav-link"><span class="nav-num">03</span> Three Strategies</a>
    </div>

    <div class="nav-group">
      <div class="nav-group-label">Your Project</div>
      <a href="#snapshot"      class="nav-link"><span class="nav-num">04</span> Project Snapshot</a>
      <a href="#model-walkthrough" class="nav-link"><span class="nav-num">05</span> Line-by-Line Model</a>
      <a href="#manager"       class="nav-link"><span class="nav-num">06</span> Manager Deep Dive</a>
    </div>

    <div class="nav-group">
      <div class="nav-group-label">Configuration</div>
      <a href="#settings"      class="nav-link"><span class="nav-num">07</span> Settings &amp; AUTH_USER_MODEL</a>
      <a href="#admin"         class="nav-link"><span class="nav-num">08</span> Superuser &amp; Admin</a>
      <a href="#migrations"    class="nav-link"><span class="nav-num">09</span> Migrations</a>
    </div>

    <div class="nav-group">
      <div class="nav-group-label">Quality</div>
      <a href="#testing"       class="nav-link"><span class="nav-num">10</span> Testing Like a Pro</a>
      <a href="#checklist"     class="nav-link"><span class="nav-num">11</span> Checklist</a>
      <a href="#blueprint"     class="nav-link"><span class="nav-num">12</span> Final Blueprint</a>
    </div>

    <div class="sidebar-footer">codeandcore.dev &copy; 2026</div>
  </nav>

  <!-- MAIN -->
  <main class="main">

    <!-- HERO -->
    <div class="hero">
      <div class="hero-eyebrow">Django Auth Deep-Dive &mdash; v1.0</div>
      <h1>The Django<br/><em>User Model</em><br/>Masterclass</h1>
      <p class="hero-desc">
        A complete teaching manual for Django&rsquo;s authentication system. From the built-in
        <code style="color:var(--gold);background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)">AbstractBaseUser</code>
        to a fully tested, admin-integrated custom user model with email login.
        Built by <strong style="color:var(--gold);font-weight:600">code::core</strong>.
      </p>
      <div class="hero-stats">
        <div class="hero-stat">
          <div class="stat-val">12</div>
          <div class="stat-label">Chapters</div>
        </div>
        <div class="hero-stat">
          <div class="stat-val">Email</div>
          <div class="stat-label">Login field</div>
        </div>
        <div class="hero-stat">
          <div class="stat-val">ABU</div>
          <div class="stat-label">AbstractBaseUser</div>
        </div>
        <div class="hero-stat">
          <div class="stat-val">core.User</div>
          <div class="stat-label">AUTH_USER_MODEL</div>
        </div>
      </div>
    </div>

    <!-- ═══ 01 ═══ MENTAL MODEL -->
    <section class="section" id="mental-model">
      <div class="section-header">
        <div class="section-num-badge">01</div>
        <div class="section-title-group">
          <div class="section-title">Mental Model</div>
          <div class="section-subtitle">Authentication vs authorisation &mdash; what Django&rsquo;s auth system actually does</div>
        </div>
      </div>

      <p>
        Django ships with a complete authentication and authorisation framework in
        <code>django.contrib.auth</code>. Before writing a single line of code it is critical to
        understand the two jobs this framework performs &mdash; they are related but distinct.
      </p>

      <div class="compare">
        <div class="compare-card bad" style="background:var(--blue-50);border-color:var(--blue-300);">
          <div class="compare-label" style="color:var(--blue-700);">&#128272; Authentication</div>
          <h4 style="color:var(--blue-700);">Who are you?</h4>
          <p>Verifying the identity of a user. Django checks credentials (email + password) and either
          confirms the identity or denies access. Managed by <code>authenticate()</code> and the login
          middleware.</p>
        </div>
        <div class="compare-card good">
          <div class="compare-label">&#128274; Authorisation</div>
          <h4>What can you do?</h4>
          <p>Once a user is known, Django decides what actions they are permitted to perform. Managed by
          the permissions system (<code>has_perm()</code>), groups, and the
          <code>PermissionsMixin</code>.</p>
        </div>
      </div>

      <div class="concept">
        <div class="concept-label">Core Concept</div>
        <h3>The Request &rarr; User Pipeline</h3>
        <p>
          Every HTTP request to a Django view passes through
          <code>django.contrib.auth.middleware.AuthenticationMiddleware</code>. This middleware
          reads the session cookie, looks up the associated user ID in the database, and attaches
          the user object to <code>request.user</code>. If no session exists,
          <code>request.user</code> is an <code>AnonymousUser</code>.
        </p>
        <p>
          When a login form is submitted, <code>authenticate(request, email=..., password=...)</code>
          is called. Django iterates <code>AUTHENTICATION_BACKENDS</code> (default:
          <code>ModelBackend</code>) until one succeeds. A successful match returns a user object;
          <code>login(request, user)</code> then writes the user ID into the session.
        </p>
      </div>

      <div class="analogy">
        <div class="analogy-label">&#128218; Mental Model</div>
        <p>
          <strong>Authentication</strong> is the hotel front desk checking your ID and giving you a key card.
          <strong>Authorisation</strong> is which doors that key card opens. Django&rsquo;s
          <code>AUTH_USER_MODEL</code> is the master register the front desk consults.
        </p>
      </div>

      <div class="callout callout-info">
        <div class="callout-icon">&#128218;</div>
        <div>
          <div class="callout-tag">Django Docs</div>
          <p>The full authentication API is documented at
          <strong>docs.djangoproject.com/en/4.2/topics/auth/</strong>.
          The customisation guide &mdash; which this masterclass follows &mdash; is at
          <strong>/topics/auth/customizing/</strong>.</p>
        </div>
      </div>
    </section>

    <hr class="rule" />

    <!-- ═══ 02 ═══ BUILT-IN USER -->
    <section class="section" id="builtin-user">
      <div class="section-header">
        <div class="section-num-badge">02</div>
        <div class="section-title-group">
          <div class="section-title">The Built-in User Model</div>
          <div class="section-subtitle">What Django gives you out of the box &mdash; and why it&rsquo;s not always enough</div>
        </div>
      </div>

      <p>
        <code>django.contrib.auth.models.User</code> is Django&rsquo;s default user model. It works
        immediately with no configuration and includes everything needed for basic authentication.
      </p>

      <div class="table-wrap">
        <table>
          <thead><tr><th>Field</th><th>Type</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td><strong>username</strong></td><td>CharField(150)</td><td>The login identifier. <strong>Not</strong> unique across Unicode normalisation.</td></tr>
            <tr><td><strong>email</strong></td><td>EmailField</td><td>Optional and <em>not</em> unique by default &mdash; multiple accounts can share an email.</td></tr>
            <tr><td><strong>first_name</strong></td><td>CharField(150)</td><td>Optional display name.</td></tr>
            <tr><td><strong>last_name</strong></td><td>CharField(150)</td><td>Optional display name.</td></tr>
            <tr><td><strong>password</strong></td><td>CharField</td><td>Stored as a hashed string. Never plain text.</td></tr>
            <tr><td><strong>is_staff</strong></td><td>BooleanField</td><td>Grants access to the Django admin site.</td></tr>
            <tr><td><strong>is_active</strong></td><td>BooleanField</td><td>Inactive users cannot log in.</td></tr>
            <tr><td><strong>is_superuser</strong></td><td>BooleanField</td><td>Bypasses all permission checks.</td></tr>
            <tr><td><strong>last_login</strong></td><td>DateTimeField</td><td>Set automatically on every successful login.</td></tr>
            <tr><td><strong>date_joined</strong></td><td>DateTimeField</td><td>Set once when the account is created.</td></tr>
          </tbody>
        </table>
      </div>

      <div class="compare">
        <div class="compare-card bad">
          <div class="compare-label">&#10005; Built-in User</div>
          <h4>Username-Centric</h4>
          <p>Users log in with a username. Email is optional and non-unique. You cannot enforce
          &ldquo;one email, one account&rdquo;. Adding fields (e.g. a profile picture or phone
          number) requires a separate <em>profile</em> model joined with a
          <code>OneToOneField</code>.</p>
        </div>
        <div class="compare-card good">
          <div class="compare-label">&#10003; Custom AbstractBaseUser</div>
          <h4>Email-First, Future-Proof</h4>
          <p>Email is the unique login identifier. Additional fields live on the same model. You
          control the schema completely. No extra joins needed. The approach used in this project
          and the one Django&rsquo;s documentation recommends for new projects.</p>
        </div>
      </div>

      <div class="callout callout-warn">
        <div class="callout-icon">&#9888;&#65039;</div>
        <div>
          <div class="callout-tag">Migration Warning</div>
          <p><strong>You cannot switch from the default User to a custom model after you have run
          your first migration.</strong> Django&rsquo;s dynamic dependency system requires
          <code>AUTH_USER_MODEL</code> to reference a model defined in the very first migration of
          its app. This project sets it up correctly from the start.</p>
        </div>
      </div>
    </section>

    <hr class="rule" />

    <!-- ═══ 03 ═══ THREE STRATEGIES -->
    <section class="section" id="strategies">
      <div class="section-header">
        <div class="section-num-badge">03</div>
        <div class="section-title-group">
          <div class="section-title">Three Strategies</div>
          <div class="section-subtitle">Proxy model, AbstractUser, or AbstractBaseUser &mdash; when to use each</div>
        </div>
      </div>

      <p>
        Django&rsquo;s documentation describes three ways to customise the user model. Each trades
        simplicity for control. Choose the right one for your project requirements.
      </p>

      <div class="step-list">
        <div class="step-card">
          <div class="step-circle">A</div>
          <div class="step-body">
            <div class="step-title">Proxy Model</div>
            <div class="step-desc">
              Subclass <code>User</code> with <code>class Meta: proxy = True</code>. The database
              table is identical to the built-in <code>auth_user</code> table &mdash; no new columns,
              no migration needed. You can add Python-only methods, change default ordering, and add
              a custom manager.
            </div>
            <div class="step-why">
              <strong>Use when:</strong> You only need to change Python behaviour (not the schema)
              and you are happy with username-based login. Good for adding
              <code>get_full_name()</code>-style helpers to an existing project.
            </div>
          </div>
        </div>
        <div class="step-card blue">
          <div class="step-circle">B</div>
          <div class="step-body">
            <div class="step-title">AbstractUser</div>
            <div class="step-desc">
              Subclass <code>django.contrib.auth.models.AbstractUser</code>. You get all the built-in
              fields (including <code>username</code>) plus the ability to add your own. One migration
              creates a new table with your extra columns.
            </div>
            <div class="step-why">
              <strong>Use when:</strong> You need extra fields (e.g. <code>bio</code>,
              <code>avatar</code>) but are happy with username-based login and Django&rsquo;s existing
              field set. Quickest path to a customisable user model.
            </div>
          </div>
        </div>
        <div class="step-card gold">
          <div class="step-circle">C</div>
          <div class="step-body">
            <div class="step-title">AbstractBaseUser &mdash; This Project</div>
            <div class="step-desc">
              Subclass <code>django.contrib.auth.models.AbstractBaseUser</code>. You own every field.
              No <code>username</code> column unless you add it. Pair with
              <code>PermissionsMixin</code> to inherit the permissions system. Requires a custom
              manager with <code>create_user()</code> and <code>create_superuser()</code>.
            </div>
            <div class="step-why">
              <strong>Use when:</strong> You want email-based login, full control over the schema, and
              future extensibility. <strong>The Django docs recommend this for all new projects.</strong>
            </div>
          </div>
        </div>
      </div>

      <div class="concept">
        <div class="concept-label">From the Django Docs</div>
        <h3>Start Every New Project With a Custom User Model</h3>
        <p>
          &ldquo;If you&rsquo;re starting a new project, it&rsquo;s highly recommended to set up a
          custom user model, even if the default User model is sufficient for you. This model behaves
          identically to the default user model, but you&rsquo;ll be able to customize it in the
          future if the need arises.&rdquo;
        </p>
        <p>
          &mdash; <em>Django 4.2 documentation, Substituting a custom User model</em>
        </p>
      </div>
    </section>

    <hr class="rule" />

    <!-- ═══ 04 ═══ PROJECT SNAPSHOT -->
    <section class="section" id="snapshot">
      <div class="section-header">
        <div class="section-num-badge">04</div>
        <div class="section-title-group">
          <div class="section-title">Project Snapshot</div>
          <div class="section-subtitle">Current state of your user model implementation &mdash; what&rsquo;s done and what&rsquo;s missing</div>
        </div>
      </div>

      <p>
        Before diving into each component, here is the honest status of the current implementation
        in <code>app/core/models.py</code> and the surrounding configuration.
      </p>

      <div class="table-wrap">
        <table>
          <thead><tr><th>Requirement</th><th>Status</th><th>Detail</th></tr></thead>
          <tbody>
            <tr>
              <td><strong>Model inherits AbstractBaseUser</strong></td>
              <td><span class="badge badge-green">&#10003; Done</span></td>
              <td><code>class User(AbstractBaseUser, PermissionsMixin)</code></td>
            </tr>
            <tr>
              <td><strong>USERNAME_FIELD = &lsquo;email&rsquo;</strong></td>
              <td><span class="badge badge-green">&#10003; Done</span></td>
              <td>Email is the unique login identifier.</td>
            </tr>
            <tr>
              <td><strong>create_user() method</strong></td>
              <td><span class="badge badge-green">&#10003; Done</span></td>
              <td>Normalises email, hashes password, saves to DB.</td>
            </tr>
            <tr>
              <td><strong>AUTH_USER_MODEL in settings.py</strong></td>
              <td><span class="badge badge-green">&#10003; Done</span></td>
              <td><code>AUTH_USER_MODEL = 'core.User'</code></td>
            </tr>
            <tr>
              <td><strong>Initial migration applied</strong></td>
              <td><span class="badge badge-green">&#10003; Done</span></td>
              <td><code>core/0001_initial</code> &mdash; model created in the first migration.</td>
            </tr>
            <tr>
              <td><strong>create_superuser() method</strong></td>
              <td><span class="badge badge-red">&#10007; Missing</span></td>
              <td>Required for the <code>createsuperuser</code> management command and CI/CD admin access.</td>
            </tr>
            <tr>
              <td><strong>Admin registration (admin.py)</strong></td>
              <td><span class="badge badge-red">&#10007; Missing</span></td>
              <td>Custom <code>UserAdmin</code> with fieldsets not yet written.</td>
            </tr>
            <tr>
              <td><strong>Redundant UserManager import</strong></td>
              <td><span class="badge badge-amber">&#9888; Warning</span></td>
              <td>Django&rsquo;s <code>UserManager</code> is imported but shadows the custom class of the same name.</td>
            </tr>
            <tr>
              <td><strong>Test suite</strong></td>
              <td><span class="badge badge-amber">&#9888; Partial</span></td>
              <td>Basic <code>create_user</code> test exists. Missing: normalisation, ValueError, superuser, __str__, admin list.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <hr class="rule" />

    <!-- ═══ 05 ═══ LINE-BY-LINE MODEL -->
    <section class="section" id="model-walkthrough">
      <div class="section-header">
        <div class="section-num-badge">05</div>
        <div class="section-title-group">
          <div class="section-title">Line-by-Line Model</div>
          <div class="section-subtitle">Every decision in models.py explained</div>
        </div>
      </div>

      <p>
        Here is the current <code>app/core/models.py</code> with every line annotated. Read this
        to understand <em>why</em> each piece exists before you modify anything.
      </p>

      <div class="code-block">
        <div class="code-top">
          <div class="code-file"><div class="code-dot"></div>app/core/models.py</div>
          <div class="code-badge">current state</div>
        </div>
        <pre><code><span class="k">from</span> django.db <span class="k">import</span> models
<span class="k">from</span> django.contrib.auth.models <span class="k">import</span> (
    AbstractBaseUser, BaseUserManager, PermissionsMixin,
    UserManager,  <span class="c"># &lt;-- PROBLEM: imports Django's UserManager, then</span>
)                 <span class="c">#              we define a class with the same name below!</span>


<span class="k">class</span> <span class="n">UserManager</span>(BaseUserManager):   <span class="c"># shadows the import above</span>
    <span class="k">def</span> <span class="f">create_user</span>(self, email, password=<span class="k">None</span>, **extra_fields):
        <span class="k">if not</span> email:
            <span class="k">raise</span> <span class="o">ValueError</span>(<span class="s">'Users must have an email address'</span>)
        user = self.model(
            email=self.normalize_email(email), **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        <span class="k">return</span> user
    <span class="c"># create_superuser() is MISSING &lt;-- must be added</span>


<span class="k">class</span> <span class="n">User</span>(AbstractBaseUser, PermissionsMixin):
    email      = models.EmailField(max_length=<span class="v">255</span>, unique=<span class="k">True</span>)
    first_name = models.CharField(max_length=<span class="v">255</span>)
    last_name  = models.CharField(max_length=<span class="v">255</span>)
    is_active  = models.BooleanField(default=<span class="k">True</span>)
    is_staff   = models.BooleanField(default=<span class="k">False</span>)

    objects = UserManager()

    USERNAME_FIELD  = <span class="s">'email'</span>
    REQUIRED_FIELDS = [<span class="s">'first_name'</span>, <span class="s">'last_name'</span>]</code></pre>
      </div>

      <div class="annotated-code">
        <div class="ann-line">
          <div class="ann-code"><span class="k">AbstractBaseUser</span></div>
          <div class="ann-text">
            <strong>The foundation.</strong> Provides <code>password</code> field (hashed),
            <code>last_login</code> field, <code>set_password()</code>, <code>check_password()</code>,
            and <code>is_authenticated</code>. Does <em>not</em> include username, email, is_staff,
            or is_superuser &mdash; those are yours to define.
          </div>
        </div>
        <div class="ann-line">
          <div class="ann-code"><span class="k">PermissionsMixin</span></div>
          <div class="ann-text">
            <strong>The permissions layer.</strong> Adds <code>is_superuser</code>,
            <code>groups</code> (ManyToMany), <code>user_permissions</code> (ManyToMany),
            <code>has_perm()</code>, and <code>has_module_perms()</code>. Without this mixin,
            you cannot use Django&rsquo;s admin or the built-in permission checks.
          </div>
        </div>
        <div class="ann-line">
          <div class="ann-code"><span class="n">USERNAME_FIELD</span> = <span class="s">'email'</span></div>
          <div class="ann-text">
            <strong>The login key.</strong> Tells Django which field to use as the unique
            identifier when calling <code>authenticate()</code>. The field must have
            <code>unique=True</code> set on the model &mdash; and our <code>email</code>
            field does.
          </div>
        </div>
        <div class="ann-line">
          <div class="ann-code"><span class="n">REQUIRED_FIELDS</span></div>
          <div class="ann-text">
            <strong>The <code>createsuperuser</code> prompts.</strong> These fields are prompted
            for interactively when running <code>python manage.py createsuperuser</code>. Must
            not include <code>USERNAME_FIELD</code> or <code>password</code> (those are always
            prompted).
          </div>
        </div>
        <div class="ann-line">
          <div class="ann-code">objects = <span class="f">UserManager</span>()</div>
          <div class="ann-text">
            <strong>The manager binding.</strong> Tells Django which manager class to use for
            <code>User.objects.create_user()</code>, <code>User.objects.create_superuser()</code>,
            and queryset operations.
          </div>
        </div>
      </div>

      <div class="callout callout-warn">
        <div class="callout-icon">&#9888;&#65039;</div>
        <div>
          <div class="callout-tag">Bug: Redundant Import</div>
          <p>The import line <code>from django.contrib.auth.models import ... UserManager</code>
          imports Django&rsquo;s built-in <code>UserManager</code> into the module namespace. The
          very next class definition <code>class UserManager(BaseUserManager)</code> immediately
          overwrites that name with the custom class. The import is harmless but misleading and
          should be removed. Fix: remove <code>UserManager</code> from the import list.</p>
        </div>
      </div>
    </section>

    <hr class="rule" />

    <!-- ═══ 06 ═══ MANAGER DEEP DIVE -->
    <section class="section" id="manager">
      <div class="section-header">
        <div class="section-num-badge">06</div>
        <div class="section-title-group">
          <div class="section-title">Manager Deep Dive</div>
          <div class="section-subtitle">How BaseUserManager works and what create_superuser must do</div>
        </div>
      </div>

      <p>
        A Django <strong>manager</strong> is the interface between a model and the database.
        <code>User.objects</code> is the manager. Every call to <code>User.objects.create_user()</code>
        goes through the manager class you define. For a custom user model, you must subclass
        <code>BaseUserManager</code> and implement at minimum two methods.
      </p>

      <div class="concept">
        <div class="concept-label">Why BaseUserManager?</div>
        <h3>Three Things It Provides</h3>
        <p>
          <strong>1. <code>normalize_email(email)</code></strong> &mdash; Lowercases the domain
          portion of the email address. <code>User@EXAMPLE.COM</code> becomes
          <code>User@example.com</code>. This prevents duplicate accounts where only capitalisation
          differs.
        </p>
        <p>
          <strong>2. <code>get_by_natural_key(username)</code></strong> &mdash; Used internally by
          Django&rsquo;s authentication backends to look up users. It queries the field named in
          <code>USERNAME_FIELD</code>.
        </p>
        <p>
          <strong>3. Queryset integration</strong> &mdash; Provides the full Django ORM queryset API
          (<code>filter()</code>, <code>get()</code>, <code>all()</code>, etc.) with the correct
          database routing via <code>using=self._db</code>.
        </p>
      </div>

      <h2>create_user() &mdash; What it does</h2>
      <div class="annotated-code">
        <div class="ann-line">
          <div class="ann-code">email = <span class="f">self.normalize_email</span>(email)</div>
          <div class="ann-text">Lowercases the domain. <code>Me@Gmail.COM</code> &rarr; <code>Me@gmail.com</code>. The local part (before @) is case-preserved per RFC 5321.</div>
        </div>
        <div class="ann-line">
          <div class="ann-code">user = <span class="f">self.model</span>(email=email, ...)</div>
          <div class="ann-text"><code>self.model</code> is the User class this manager is attached to. This calls <code>User(email=..., ...)</code> without saving to the DB yet.</div>
        </div>
        <div class="ann-line">
          <div class="ann-code">user.<span class="f">set_password</span>(password)</div>
          <div class="ann-text">Hashes the raw password string using PBKDF2-SHA256 (Django&rsquo;s default hasher). The raw string is never stored. Passing <code>None</code> marks the account as having no usable password.</div>
        </div>
        <div class="ann-line">
          <div class="ann-code">user.<span class="f">save</span>(using=self._db)</div>
          <div class="ann-text"><code>using=self._db</code> routes the save to the correct database in multi-database configurations. Always use this pattern in managers; never call <code>user.save()</code> alone.</div>
        </div>
      </div>

      <h2>create_superuser() &mdash; The Missing Method</h2>
      <p>
        The <code>createsuperuser</code> management command calls
        <code>UserManager.create_superuser()</code>. Without it, running
        <code>python manage.py createsuperuser</code> raises an <code>AttributeError</code>. The
        implementation is straightforward &mdash; call <code>create_user()</code> and set the
        required flags:
      </p>

      <div class="code-block">
        <div class="code-top">
          <div class="code-file"><div class="code-dot"></div>app/core/models.py &mdash; add this method to UserManager</div>
          <div class="code-badge">fix required</div>
        </div>
        <pre><code>    <span class="k">def</span> <span class="f">create_superuser</span>(self, email, password=<span class="k">None</span>, **extra_fields):
        extra_fields.setdefault(<span class="s">'is_staff'</span>,     <span class="k">True</span>)
        extra_fields.setdefault(<span class="s">'is_superuser'</span>, <span class="k">True</span>)

        <span class="k">if</span> extra_fields.get(<span class="s">'is_staff'</span>) <span class="k">is not True</span>:
            <span class="k">raise</span> <span class="o">ValueError</span>(<span class="s">'Superuser must have is_staff=True.'</span>)
        <span class="k">if</span> extra_fields.get(<span class="s">'is_superuser'</span>) <span class="k">is not True</span>:
            <span class="k">raise</span> <span class="o">ValueError</span>(<span class="s">'Superuser must have is_superuser=True.'</span>)

        <span class="k">return</span> self.<span class="f">create_user</span>(email, password, **extra_fields)</code></pre>
      </div>

      <div class="callout callout-info">
        <div class="callout-icon">&#128161;</div>
        <div>
          <div class="callout-tag">Why setdefault?</div>
          <p>Using <code>setdefault()</code> means the caller can still override the flags
          programmatically (e.g. in tests) without triggering the validation error. The guards
          (<code>if ... is not True</code>) protect against accidentally creating a superuser with
          <code>is_superuser=False</code> via direct keyword arguments.</p>
        </div>
      </div>
    </section>

    <hr class="rule" />

    <!-- ═══ 07 ═══ SETTINGS -->
    <section class="section" id="settings">
      <div class="section-header">
        <div class="section-num-badge">07</div>
        <div class="section-title-group">
          <div class="section-title">Settings &amp; AUTH_USER_MODEL</div>
          <div class="section-subtitle">The one setting that must be set before the first migration</div>
        </div>
      </div>

      <p>
        <code>AUTH_USER_MODEL</code> tells Django which model to use for all user-related
        operations. It must be set to an <code>'app_label.ModelName'</code> string that resolves
        to a concrete model class.
      </p>

      <div class="code-block">
        <div class="code-top">
          <div class="code-file"><div class="code-dot"></div>app/app/settings.py</div>
          <div class="code-badge">already set &#10003;</div>
        </div>
        <pre><code><span class="c"># Tells all of Django's auth machinery to use our User model</span>
<span class="n">AUTH_USER_MODEL</span> = <span class="s">'core.User'</span>   <span class="c"># 'core' is the app label, 'User' is the class</span></code></pre>
      </div>

      <div class="concept">
        <div class="concept-label">What This Setting Does</div>
        <h3>Where AUTH_USER_MODEL Is Used</h3>
        <p>
          Every part of Django that touches users reads this setting instead of hard-coding
          <code>auth.User</code>:
        </p>
        <ul>
          <li><code>django.contrib.auth.get_user_model()</code> returns your class</li>
          <li>The admin&rsquo;s login page authenticates against your model</li>
          <li>Session middleware loads your user on every request</li>
          <li><code>ForeignKey(settings.AUTH_USER_MODEL, ...)</code> in other apps resolves to your model</li>
          <li><code>createsuperuser</code> and <code>changepassword</code> management commands use your manager</li>
        </ul>
      </div>

      <div class="callout callout-danger">
        <div class="callout-icon">&#128683;</div>
        <div>
          <div class="callout-tag">Do Not Change After Migrations</div>
          <p><strong>Changing <code>AUTH_USER_MODEL</code> after your first <code>migrate</code>
          run is extremely difficult.</strong> Foreign keys in <code>auth_permission</code>,
          <code>auth_group</code>, and any other app that references the user model will become
          orphaned. You would need to manually rename tables, update foreign keys, and rewrite
          migrations. Always set this setting before running <code>migrate</code> for the first time.
          This project follows that rule.</p>
        </div>
      </div>

      <h2>Referencing the User Model in Other Apps</h2>
      <p>
        Never import <code>from django.contrib.auth.models import User</code> in your own app code.
        If <code>AUTH_USER_MODEL</code> is ever changed (or in reusable packages), that import
        breaks. Use one of these patterns instead:
      </p>

      <div class="code-block">
        <div class="code-top">
          <div class="code-file"><div class="code-dot"></div>Correct ways to reference the User model</div>
          <div class="code-badge">best practice</div>
        </div>
        <pre><code><span class="c"># Option 1: ForeignKey / relations &mdash; use settings directly</span>
<span class="k">from</span> django.conf <span class="k">import</span> settings

<span class="k">class</span> <span class="n">Recipe</span>(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,   <span class="c"># resolved at runtime to core.User</span>
        on_delete=models.CASCADE,
    )

<span class="c"># Option 2: Runtime model class &mdash; e.g. in views or serializers</span>
<span class="k">from</span> django.contrib.auth <span class="k">import</span> get_user_model

User = <span class="f">get_user_model</span>()   <span class="c"># returns the currently active user model class</span></code></pre>
      </div>
    </section>

    <hr class="rule" />

    <!-- ═══ 08 ═══ ADMIN -->
    <section class="section" id="admin">
      <div class="section-header">
        <div class="section-num-badge">08</div>
        <div class="section-title-group">
          <div class="section-title">Superuser &amp; Admin</div>
          <div class="section-subtitle">Registering your custom User model with Django&rsquo;s admin site</div>
        </div>
      </div>

      <p>
        Once <code>create_superuser()</code> is in place you can create an admin account.
        But the admin site will refuse to display your user model unless you register it with
        a custom <code>UserAdmin</code> class that understands your fields.
      </p>

      <div class="callout callout-info">
        <div class="callout-icon">&#128218;</div>
        <div>
          <div class="callout-tag">Why a custom UserAdmin?</div>
          <p>The built-in <code>django.contrib.auth.admin.UserAdmin</code> references fields like
          <code>username</code> that do not exist on your model. You must subclass it and replace
          <code>fieldsets</code>, <code>add_fieldsets</code>, <code>list_display</code>, and
          <code>ordering</code> to point to your actual fields.</p>
        </div>
      </div>

      <div class="code-block">
        <div class="code-top">
          <div class="code-file"><div class="code-dot"></div>app/core/admin.py &mdash; full implementation</div>
          <div class="code-badge">write this</div>
        </div>
        <pre><code><span class="k">from</span> django.contrib <span class="k">import</span> admin
<span class="k">from</span> django.contrib.auth.admin <span class="k">import</span> UserAdmin <span class="k">as</span> BaseUserAdmin
<span class="k">from</span> django.utils.translation <span class="k">import</span> gettext_lazy <span class="k">as</span> _

<span class="k">from</span> core.models <span class="k">import</span> User


<span class="k">class</span> <span class="n">UserAdmin</span>(BaseUserAdmin):
    ordering    = [<span class="s">'id'</span>]
    list_display = [<span class="s">'email'</span>, <span class="s">'first_name'</span>, <span class="s">'last_name'</span>, <span class="s">'is_staff'</span>]

    fieldsets = (
        (<span class="k">None</span>, {<span class="s">'fields'</span>: (<span class="s">'email'</span>, <span class="s">'password'</span>)}),
        (_(<span class="s">'Personal Info'</span>), {<span class="s">'fields'</span>: (<span class="s">'first_name'</span>, <span class="s">'last_name'</span>)}),
        (
            _(<span class="s">'Permissions'</span>),
            {<span class="s">'fields'</span>: (<span class="s">'is_active'</span>, <span class="s">'is_staff'</span>, <span class="s">'is_superuser'</span>)},
        ),
        (_(<span class="s">'Important dates'</span>), {<span class="s">'fields'</span>: (<span class="s">'last_login'</span>,)}),
    )

    readonly_fields = [<span class="s">'last_login'</span>]

    add_fieldsets = (
        (<span class="k">None</span>, {
            <span class="s">'classes'</span>: (<span class="s">'wide'</span>,),
            <span class="s">'fields'</span>: (
                <span class="s">'email'</span>, <span class="s">'password1'</span>, <span class="s">'password2'</span>,
                <span class="s">'first_name'</span>, <span class="s">'last_name'</span>,
                <span class="s">'is_active'</span>, <span class="s">'is_staff'</span>, <span class="s">'is_superuser'</span>,
            ),
        }),
    )


admin.site.register(User, UserAdmin)</code></pre>
      </div>

      <div class="analogy">
        <div class="analogy-label">&#128218; Why readonly_fields = [&lsquo;last_login&rsquo;]</div>
        <p>
          <code>last_login</code> is provided by <code>AbstractBaseUser</code> and updated
          automatically on every login. It is not something an admin should edit directly.
          Marking it <code>readonly</code> keeps it visible in the admin without allowing accidental
          modification.
        </p>
      </div>

      <h2>Create Your First Superuser</h2>
      <div class="code-block">
        <div class="code-top">
          <div class="code-file"><div class="code-dot"></div>Shell &mdash; inside Docker</div>
          <div class="code-badge">commands</div>
        </div>
        <pre><code><span class="c"># Start the stack</span>
docker compose up -d

<span class="c"># Create superuser interactively</span>
docker compose run --rm app sh -c <span class="s">"python manage.py createsuperuser"</span>

<span class="c"># Open the admin at http://localhost:8000/admin/</span></code></pre>
      </div>
    </section>

    <hr class="rule" />

    <!-- ═══ 09 ═══ MIGRATIONS -->
    <section class="section" id="migrations">
      <div class="section-header">
        <div class="section-num-badge">09</div>
        <div class="section-title-group">
          <div class="section-title">Migrations</div>
          <div class="section-subtitle">Order matters &mdash; the auth model must be in 0001_initial</div>
        </div>
      </div>

      <p>
        Django&rsquo;s migration system generates SQL from your model definitions. For a custom user
        model there is one non-negotiable rule: the model must be defined in the <em>first</em>
        migration of its app.
      </p>

      <div class="concept">
        <div class="concept-label">Why first migration?</div>
        <h3>Django&rsquo;s Swappable Model Dependency</h3>
        <p>
          Django uses a &ldquo;swappable&rdquo; dependency mechanism for <code>AUTH_USER_MODEL</code>.
          When other apps (like <code>django.contrib.auth</code> itself) create foreign keys to the
          user model, they generate a dependency in their migrations to the app and migration number
          that created the user model.
        </p>
        <p>
          If the user model is not in <code>0001_initial</code> &mdash; for example if it is in
          <code>0003_add_user</code> &mdash; Django cannot resolve the dependency and raises a
          <code>CircularDependencyError</code>. This project has it correctly placed in
          <code>core/0001_initial.py</code>.
        </p>
      </div>

      <div class="code-block">
        <div class="code-top">
          <div class="code-file"><div class="code-dot"></div>Migration commands</div>
          <div class="code-badge">reference</div>
        </div>
        <pre><code><span class="c"># Generate migration files from model changes</span>
docker compose run --rm app sh -c <span class="s">"python manage.py makemigrations"</span>

<span class="c"># Apply all pending migrations to the database</span>
docker compose run --rm app sh -c <span class="s">"python manage.py migrate"</span>

<span class="c"># Show all migrations and their applied status</span>
docker compose run --rm app sh -c <span class="s">"python manage.py showmigrations"</span>

<span class="c"># Expected output for this project:</span>
<span class="c"># core</span>
<span class="c">#   [X] 0001_initial</span></code></pre>
      </div>

      <div class="callout callout-warn">
        <div class="callout-icon">&#9888;&#65039;</div>
        <div>
          <div class="callout-tag">Never Edit Applied Migrations</div>
          <p>Once a migration has been applied to any database (dev, CI, staging, production),
          treat it as immutable. If you need to change the schema, always create a <strong>new</strong>
          migration. Editing applied migrations corrupts the migration history and can break
          deployments irreversibly.</p>
        </div>
      </div>
    </section>

    <hr class="rule" />

    <!-- ═══ 10 ═══ TESTING -->
    <section class="section" id="testing">
      <div class="section-header">
        <div class="section-num-badge">10</div>
        <div class="section-title-group">
          <div class="section-title">Testing Like a Pro</div>
          <div class="section-subtitle">A complete test suite for the custom user model</div>
        </div>
      </div>

      <p>
        The existing test covers basic user creation but misses several critical paths. A
        production-grade test suite must cover all the behaviours your model promises.
      </p>

      <div class="code-block">
        <div class="code-top">
          <div class="code-file"><div class="code-dot"></div>app/core/tests/test_models.py &mdash; complete suite</div>
          <div class="code-badge">write this</div>
        </div>
        <pre><code><span class="k">from</span> django.test <span class="k">import</span> TestCase
<span class="k">from</span> django.contrib.auth <span class="k">import</span> get_user_model


<span class="k">class</span> <span class="n">ModelTests</span>(TestCase):

    <span class="k">def</span> <span class="f">test_create_user_with_email_successful</span>(self):
        <span class="s">'''Create a user with an email is successful.'''</span>
        email    = <span class="s">'test@example.com'</span>
        password = <span class="s">'testpass123'</span>
        user = get_user_model().objects.<span class="f">create_user</span>(
            email=email,
            password=password,
        )
        self.<span class="f">assertEqual</span>(user.email, email)
        self.<span class="f">assertTrue</span>(user.<span class="f">check_password</span>(password))

    <span class="k">def</span> <span class="f">test_new_user_email_normalized</span>(self):
        <span class="s">'''Email domain is lowercased on creation.'''</span>
        sample_emails = [
            [<span class="s">'test1@EXAMPLE.com'</span>, <span class="s">'test1@example.com'</span>],
            [<span class="s">'Test2@Example.com'</span>, <span class="s">'Test2@example.com'</span>],
            [<span class="s">'TEST3@EXAMPLE.COM'</span>, <span class="s">'TEST3@example.com'</span>],
        ]
        <span class="k">for</span> email, expected <span class="k">in</span> sample_emails:
            user = get_user_model().objects.<span class="f">create_user</span>(email, <span class="s">'sample123'</span>)
            self.<span class="f">assertEqual</span>(user.email, expected)

    <span class="k">def</span> <span class="f">test_new_user_without_email_raises_error</span>(self):
        <span class="s">'''Creating a user without an email raises ValueError.'''</span>
        <span class="k">with</span> self.<span class="f">assertRaises</span>(ValueError):
            get_user_model().objects.<span class="f">create_user</span>(<span class="s">''</span>, <span class="s">'test123'</span>)

    <span class="k">def</span> <span class="f">test_create_superuser</span>(self):
        <span class="s">'''Create a superuser with is_staff and is_superuser True.'''</span>
        user = get_user_model().objects.<span class="f">create_superuser</span>(
            email=<span class="s">'super@example.com'</span>,
            password=<span class="s">'testpass123'</span>,
        )
        self.<span class="f">assertTrue</span>(user.is_superuser)
        self.<span class="f">assertTrue</span>(user.is_staff)

    <span class="k">def</span> <span class="f">test_user_str_returns_email</span>(self):
        <span class="s">'''The string representation of a user is their email.'''</span>
        user = get_user_model().objects.<span class="f">create_user</span>(
            email=<span class="s">'test@example.com'</span>,
            password=<span class="s">'testpass123'</span>,
        )
        self.<span class="f">assertEqual</span>(<span class="f">str</span>(user), user.email)</code></pre>
      </div>

      <div class="callout callout-info">
        <div class="callout-icon">&#128161;</div>
        <div>
          <div class="callout-tag">Note: __str__ not yet defined</div>
          <p>The <code>test_user_str_returns_email</code> test will fail until you add
          <code>def __str__(self): return self.email</code> to the <code>User</code> class.
          Without it, <code>str(user)</code> returns something like
          <code>'core.User.None'</code>. Add the method and re-run the tests.</p>
        </div>
      </div>

      <div class="code-block">
        <div class="code-top">
          <div class="code-file"><div class="code-dot"></div>Run the tests</div>
          <div class="code-badge">commands</div>
        </div>
        <pre><code><span class="c"># Run the full test suite inside Docker</span>
docker compose run --rm app sh -c <span class="s">"python manage.py test"</span>

<span class="c"># Run only the core app tests</span>
docker compose run --rm app sh -c <span class="s">"python manage.py test core"</span>

<span class="c"># Run with verbose output</span>
docker compose run --rm app sh -c <span class="s">"python manage.py test core --verbosity=2"</span></code></pre>
      </div>
    </section>

    <hr class="rule" />

    <!-- ═══ 11 ═══ CHECKLIST -->
    <section class="section" id="checklist">
      <div class="section-header">
        <div class="section-num-badge">11</div>
        <div class="section-title-group">
          <div class="section-title">Checklist</div>
          <div class="section-subtitle">Everything required for a production-grade custom user model</div>
        </div>
      </div>

      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Item</th><th>File</th><th>Status</th><th>Action required</th></tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Set AUTH_USER_MODEL before first migration</strong></td>
              <td><code>settings.py</code></td>
              <td><span class="badge badge-green">&#10003; Done</span></td>
              <td>&mdash;</td>
            </tr>
            <tr>
              <td><strong>Model in 0001_initial migration</strong></td>
              <td><code>core/migrations/</code></td>
              <td><span class="badge badge-green">&#10003; Done</span></td>
              <td>&mdash;</td>
            </tr>
            <tr>
              <td><strong>AbstractBaseUser + PermissionsMixin</strong></td>
              <td><code>core/models.py</code></td>
              <td><span class="badge badge-green">&#10003; Done</span></td>
              <td>&mdash;</td>
            </tr>
            <tr>
              <td><strong>USERNAME_FIELD = &lsquo;email&rsquo;</strong></td>
              <td><code>core/models.py</code></td>
              <td><span class="badge badge-green">&#10003; Done</span></td>
              <td>&mdash;</td>
            </tr>
            <tr>
              <td><strong>create_user() normalises email</strong></td>
              <td><code>core/models.py</code></td>
              <td><span class="badge badge-green">&#10003; Done</span></td>
              <td>&mdash;</td>
            </tr>
            <tr>
              <td><strong>create_superuser() method</strong></td>
              <td><code>core/models.py</code></td>
              <td><span class="badge badge-red">&#10007; Missing</span></td>
              <td>Add to <code>UserManager</code> &mdash; see Chapter 06</td>
            </tr>
            <tr>
              <td><strong>__str__ returns email</strong></td>
              <td><code>core/models.py</code></td>
              <td><span class="badge badge-red">&#10007; Missing</span></td>
              <td>Add <code>def __str__(self): return self.email</code> to <code>User</code></td>
            </tr>
            <tr>
              <td><strong>Remove redundant UserManager import</strong></td>
              <td><code>core/models.py</code></td>
              <td><span class="badge badge-amber">&#9888; Warning</span></td>
              <td>Remove <code>UserManager</code> from the import list</td>
            </tr>
            <tr>
              <td><strong>Custom UserAdmin registered</strong></td>
              <td><code>core/admin.py</code></td>
              <td><span class="badge badge-red">&#10007; Missing</span></td>
              <td>Create <code>core/admin.py</code> &mdash; see Chapter 08</td>
            </tr>
            <tr>
              <td><strong>Full test suite</strong></td>
              <td><code>core/tests/</code></td>
              <td><span class="badge badge-amber">&#9888; Partial</span></td>
              <td>Add normalisation, ValueError, superuser, __str__ tests &mdash; see Chapter 10</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <hr class="rule" />

    <!-- ═══ 12 ═══ FINAL BLUEPRINT -->
    <section class="section" id="blueprint">
      <div class="section-header">
        <div class="section-num-badge">12</div>
        <div class="section-title-group">
          <div class="section-title">Final Blueprint</div>
          <div class="section-subtitle">The ordered steps to implement a complete, tested custom user model from scratch</div>
        </div>
      </div>

      <p>
        Use this as your recipe for every new Django project. Follow the steps in order &mdash;
        the migration step especially cannot be moved.
      </p>

      <div class="step-list">
        <div class="step-card gold">
          <div class="step-circle">1</div>
          <div class="step-body">
            <div class="step-title">Create the app and add to INSTALLED_APPS</div>
            <div class="step-desc"><code>python manage.py startapp core</code>. Add <code>'core'</code> to <code>INSTALLED_APPS</code> in <code>settings.py</code>.</div>
          </div>
        </div>
        <div class="step-card gold">
          <div class="step-circle">2</div>
          <div class="step-body">
            <div class="step-title">Set AUTH_USER_MODEL <em>immediately</em></div>
            <div class="step-desc">Before writing a single model or running any migration, add <code>AUTH_USER_MODEL = 'core.User'</code> to <code>settings.py</code>. This is the only step order that cannot be changed.</div>
            <div class="step-why"><strong>Why:</strong> Django&rsquo;s migration graph resolves the user model at migration creation time. Setting this after the first migration requires manual schema repair.</div>
          </div>
        </div>
        <div class="step-card">
          <div class="step-circle">3</div>
          <div class="step-body">
            <div class="step-title">Write the UserManager with both create methods</div>
            <div class="step-desc">Subclass <code>BaseUserManager</code>. Implement <code>create_user()</code> (normalise email, hash password, save) and <code>create_superuser()</code> (delegate to create_user + set flags).</div>
          </div>
        </div>
        <div class="step-card">
          <div class="step-circle">4</div>
          <div class="step-body">
            <div class="step-title">Write the User model</div>
            <div class="step-desc">Subclass <code>AbstractBaseUser</code> and <code>PermissionsMixin</code>. Define your fields. Set <code>USERNAME_FIELD</code>, <code>REQUIRED_FIELDS</code>, <code>objects = UserManager()</code>. Add <code>__str__</code>.</div>
          </div>
        </div>
        <div class="step-card">
          <div class="step-circle">5</div>
          <div class="step-body">
            <div class="step-title">Run makemigrations &mdash; verify it creates 0001_initial</div>
            <div class="step-desc"><code>python manage.py makemigrations core</code>. Inspect the generated file to confirm the User model is defined in it. Then <code>python manage.py migrate</code>.</div>
          </div>
        </div>
        <div class="step-card">
          <div class="step-circle">6</div>
          <div class="step-body">
            <div class="step-title">Write tests for create_user, normalisation, ValueError, superuser, __str__</div>
            <div class="step-desc">Use <code>get_user_model()</code> in tests. Run: <code>python manage.py test core</code>. All five test cases from Chapter 10 must pass.</div>
          </div>
        </div>
        <div class="step-card blue">
          <div class="step-circle">7</div>
          <div class="step-body">
            <div class="step-title">Write and register the custom UserAdmin</div>
            <div class="step-desc">Create <code>core/admin.py</code>. Subclass <code>BaseUserAdmin</code>. Set <code>fieldsets</code>, <code>add_fieldsets</code>, <code>list_display</code>, <code>ordering</code>, <code>readonly_fields</code>. Register with <code>admin.site.register(User, UserAdmin)</code>.</div>
            <div class="step-why"><strong>Verify:</strong> <code>python manage.py createsuperuser</code>, then open <code>/admin/</code> and confirm the user list displays correctly.</div>
          </div>
        </div>
      </div>

      <div class="callout callout-success">
        <div class="callout-icon">&#10003;</div>
        <div>
          <div class="callout-tag">You&rsquo;re Done When&hellip;</div>
          <p>All tests pass. <code>python manage.py createsuperuser</code> works. The admin shows
          your user list with email, first_name, last_name, is_staff. Every item in the Chapter 11
          checklist shows a green badge.</p>
        </div>
      </div>
    </section>

    <!-- FOOTER -->
    <footer class="footer">
      <div class="footer-brand">code<span>::</span>core</div>
      <p>Django User Model Masterclass &mdash; codeandcore.dev</p>
    </footer>

  </main>
</div>

<script>
  // Active nav on scroll
  const sections = document.querySelectorAll('.section[id]');
  const links    = document.querySelectorAll('.nav-link');

  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        links.forEach(l => l.classList.remove('active'));
        const a = document.querySelector(`.nav-link[href="#${e.target.id}"]`);
        if (a) a.classList.add('active');
      }
    });
  }, { threshold: 0.35 });

  sections.forEach(s => obs.observe(s));

  // Copy buttons
  document.querySelectorAll('.code-block pre').forEach(pre => {
    const btn = document.createElement('button');
    btn.textContent = 'Copy';
    btn.style.cssText = [
      'position:absolute', 'top:.55rem', 'right:.75rem',
      'font-family:Jost,sans-serif', 'font-size:10px', 'font-weight:600',
      'letter-spacing:.1em', 'text-transform:uppercase',
      'background:rgba(255,255,255,.08)', 'color:rgba(255,255,255,.45)',
      'border:1px solid rgba(255,255,255,.12)', 'border-radius:4px',
      'padding:.25rem .6rem', 'cursor:pointer', 'transition:all .15s',
    ].join(';');
    btn.addEventListener('click', () => {
      navigator.clipboard.writeText(pre.innerText).then(() => {
        btn.textContent = 'Copied!';
        btn.style.color = 'var(--gold)';
        setTimeout(() => { btn.textContent = 'Copy'; btn.style.color = 'rgba(255,255,255,.45)'; }, 1500);
      });
    });
    pre.parentElement.style.position = 'relative';
    pre.parentElement.appendChild(btn);
  });
</script>
</body>
</html>"""

out = pathlib.Path(r"d:\Projects\recipe-app-api\usermodel.html")
out.write_text(HTML, encoding="utf-8")
print(f"Written {out} ({out.stat().st_size:,} bytes)")
