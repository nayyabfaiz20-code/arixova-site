from html import escape
from pathlib import Path


ROOT = Path(__file__).parent
SERVICES = [
    {
        "slug": "web-development",
        "name": "Website Development",
        "short": "A clear, fast website that helps the right customers take the next step.",
        "promise": "Build a website that makes your business easier to choose.",
        "intro": "We design and build business websites and web applications that explain what you do, work beautifully on mobile and make it simple to enquire or buy.",
        "problems": [
            "Your website no longer reflects the quality of your work.",
            "Visitors cannot quickly find the information or action they need.",
            "Your team relies on a developer for every content change.",
            "You need a booking, enquiry or online payment journey that fits your business.",
        ],
        "deliverables": [
            "Responsive business websites and web applications",
            "E-commerce, booking and enquiry journeys",
            "Content management setup for everyday edits",
            "Technical search foundations, accessibility and performance checks",
            "Launch support, documentation and team handover",
        ],
        "examples": [
            "A service business replaces an ageing website with clearer service pages and a simpler quote-request journey.",
            "A distributor gives customers a searchable product catalogue and a straightforward route to request a quote.",
        ],
        "benefit": "Customers get a clearer picture of your offer. Your team gets a maintainable site built around real business needs.",
        "need": "A sense of your audience, goals and existing brand or website. We can help shape the brief if those are still taking form.",
        "faqs": [
            ("How much does a website cost?", "The cost depends on the pages, integrations and features involved. We agree a clear scope and quote before work begins."),
            ("How long will it take?", "Timing depends on the scope and how quickly content and feedback are available. We set a realistic schedule after discovery."),
            ("Can we edit the site ourselves?", "Yes. Where appropriate, we set up a content management system and show your team how to use it."),
            ("Who owns the finished website?", "Ownership, access and any third-party licence costs are agreed clearly as part of the project."),
        ],
    },
    {
        "slug": "website-management",
        "name": "Website Management",
        "short": "Keep your website maintained, accurate and working without adding to your team’s workload.",
        "promise": "Keep your website looked after, not left behind.",
        "intro": "We provide ongoing website care for teams that need updates, maintenance and practical support without managing every small task themselves.",
        "problems": [
            "Software updates are repeatedly postponed.",
            "Small content changes turn into a long queue of requests.",
            "You are unsure whether backups and monitoring are in place.",
            "When something breaks, nobody is clearly responsible.",
        ],
        "deliverables": [
            "Agreed content, image and landing-page edits",
            "Routine software and dependency updates",
            "Backup checks and basic site-health monitoring",
            "Bug investigation and fixes within the agreed scope",
            "Regular review of performance and improvement priorities",
        ],
        "examples": [
            "A growing company arranges regular updates, maintenance checks and campaign-page changes through one agreed support plan.",
            "An organisation schedules routine content reviews so key information stays current throughout the year.",
        ],
        "benefit": "Your website stays more current and your team has a clear route for everyday changes and issues.",
        "need": "Website access, hosting details and a list of the issues or recurring tasks that take up your time.",
        "faqs": [
            ("What does a support plan include?", "The plan is agreed around your platform, priorities and expected requests. The scope and any limits are documented before it starts."),
            ("Can you manage a website you did not build?", "Often, yes. We first review how it is built, who hosts it and whether we can safely take responsibility for it."),
            ("Do you guarantee that a website will never go down?", "No service can responsibly promise that. We can agree monitoring, backup and response procedures appropriate to your site."),
            ("Can I request one-off changes?", "Yes. One-off work can be discussed separately if ongoing support is not the right fit."),
        ],
    },
    {
        "slug": "custom-tools",
        "name": "Custom Tools",
        "short": "Replace repetitive spreadsheets and disconnected processes with tools shaped around your work.",
        "promise": "Make the way your business works easier to manage.",
        "intro": "When off-the-shelf software or spreadsheets no longer fit, we build practical internal tools around the people, information and processes you already have.",
        "problems": [
            "The same information is copied between spreadsheets and systems.",
            "Staff depend on manual workarounds to get routine jobs done.",
            "Managers cannot see the latest operational picture in one place.",
            "Customers or colleagues need a secure way to submit or track information.",
        ],
        "deliverables": [
            "Internal dashboards and staff portals",
            "Quoting, booking and calculation tools",
            "Customer portals and structured data-entry forms",
            "Connections to suitable existing systems",
            "Documentation, access controls and team handover",
        ],
        "examples": [
            "A logistics team brings job status and staff availability into one internal dashboard instead of updating several separate sheets.",
            "A service team uses a shared quoting tool to capture consistent information before preparing a proposal.",
        ],
        "benefit": "Information is easier to find, routine work is more consistent and the tool reflects your actual process.",
        "need": "A walkthrough of the current process, the people involved and the systems or data the tool may need to connect to.",
        "faqs": [
            ("Do we need a detailed specification?", "No. A discovery session can turn your current process and pain points into a practical first scope."),
            ("Can a custom tool connect to our existing software?", "That depends on the systems and the access they provide. We check integration options early and explain any limitations."),
            ("Will it work on phones and tablets?", "We agree the devices and tasks it needs to support, then design the interface around them."),
            ("Who maintains the tool after launch?", "Support and ownership arrangements are agreed before development, so you know how updates will be handled."),
        ],
    },
    {
        "slug": "ai-integration",
        "name": "AI Integration",
        "short": "Introduce useful AI to existing work, with clear safeguards and people in control.",
        "promise": "Put AI to work on a real business task.",
        "intro": "We help identify suitable AI uses, connect them to existing workflows and build in review, privacy and operational safeguards from the outset.",
        "problems": [
            "Your team spends time searching documents or drafting repetitive replies.",
            "AI experiments are not connected to an actual business process.",
            "You need people to review AI-generated answers before they are used.",
            "You want to understand data handling before choosing a tool or model.",
        ],
        "deliverables": [
            "A practical use-case and data-readiness assessment",
            "Knowledge assistants based on approved information",
            "Document summaries, extraction or support triage",
            "Human review, permissions and error-handling steps",
            "A measured rollout plan with clear limits and ownership",
        ],
        "examples": [
            "A support team drafts replies from approved company guidance, while staff review sensitive responses before they are sent.",
            "An operations team extracts standard fields from supplier documents and checks the results before they enter a system.",
        ],
        "benefit": "AI supports a defined task while your people retain visibility and responsibility for important decisions.",
        "need": "A specific task to explore, examples of the information involved and your expectations for review and data handling.",
        "faqs": [
            ("Will AI always give the right answer?", "No. AI can make mistakes. We design suitable review and escalation steps and make limitations clear."),
            ("Can you use our internal documents?", "Possibly, subject to the selected tools, permissions and data-handling arrangements. We assess this before implementation."),
            ("Do we need to replace our existing software?", "Not necessarily. Some solutions can be added to existing workflows; feasibility depends on your systems."),
            ("How do you decide if AI is worthwhile?", "We start with the task, likely value, risks and alternatives. If a simpler approach is better, we will say so."),
        ],
    },
    {
        "slug": "workflow-automation",
        "name": "Workflow Automation",
        "short": "Connect everyday tools to reduce rekeying, missed handovers and repetitive administration.",
        "promise": "Let routine work move between your systems.",
        "intro": "We map how work moves through your business, then connect suitable tools so routine updates, notifications and handovers happen more consistently.",
        "problems": [
            "Information from a form has to be typed into another system.",
            "A handover depends on someone remembering to send a message.",
            "Approvals get stuck in inboxes without a clear status.",
            "Reports take too long to assemble from separate tools.",
        ],
        "deliverables": [
            "A map of the current workflow and handover points",
            "Form-to-system and customer relationship management connections",
            "Lead routing, task creation and notifications",
            "Approval steps, error alerts and activity records",
            "Testing, documentation and an agreed monitoring approach",
        ],
        "examples": [
            "A website enquiry creates a lead in the company’s customer system and notifies the appropriate team member.",
            "An approval request moves to the next reviewer, with a reminder and a visible status for the team.",
        ],
        "benefit": "Routine information moves with fewer manual steps, while exceptions remain visible to the people who need to act.",
        "need": "A walkthrough of the current process, the tools involved and any approval, privacy or audit requirements.",
        "faqs": [
            ("Which apps can you connect?", "It depends on the tools and the integration options they provide. We confirm feasibility before agreeing the build."),
            ("What happens when an automation fails?", "We design suitable error notifications and recovery steps so failures can be identified and handled."),
            ("Will automation remove the need for staff review?", "Not always. We keep human checks where judgement, approval or sensitive information requires them."),
            ("Can you change an existing automated workflow?", "Yes, after reviewing how it works, who depends on it and how failures are currently handled."),
        ],
    },
    {
        "slug": "digital-strategy",
        "name": "Digital Strategy",
        "short": "Decide what to improve, build or automate first—with a plan your team can act on.",
        "promise": "Make your next technology decision with a clearer plan.",
        "intro": "We help business leaders understand their current setup, set priorities and plan sensible technology improvements without adding complexity for its own sake.",
        "problems": [
            "Several possible investments compete for the same budget.",
            "The current systems are difficult to understand or maintain.",
            "You are unsure whether to build, buy or improve what you have.",
            "A technology project needs clearer scope before approval.",
        ],
        "deliverables": [
            "A focused review of the current digital setup",
            "A prioritised list of opportunities and risks",
            "Build-versus-buy and platform considerations",
            "A phased roadmap with practical next steps",
            "Budget, dependency and implementation questions to resolve",
        ],
        "examples": [
            "A growing business receives a phased plan for improving its website, customer system and enquiry handling.",
            "A leadership team compares buying and building options before committing to a new scheduling system.",
        ],
        "benefit": "Your team can compare options, understand trade-offs and focus effort on the next useful step.",
        "need": "Your goals, current constraints, existing tools and the decisions you need to make.",
        "faqs": [
            ("Do you recommend particular vendors?", "Recommendations are based on the needs and constraints discussed. We explain the reasoning and relevant trade-offs."),
            ("Will you also implement the roadmap?", "That can be discussed, but the strategy work is useful on its own and does not commit you to implementation."),
            ("How long does a strategy engagement take?", "It depends on the number of systems and stakeholders. We agree the scope and schedule before starting."),
            ("What do we receive at the end?", "The outputs are agreed up front and may include findings, priorities, decision notes and an implementation roadmap."),
        ],
    },
]


def icon(name: str) -> str:
    paths = {
        "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
        "spark": '<path d="m12 3 1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8L12 3Z"/><path d="m19 14 .9 2.1L22 17l-2.1.9L19 20l-.9-2.1L16 17l2.1-.9L19 14Z"/>',
        "grid": '<rect x="4" y="4" width="6" height="6" rx="1"/><rect x="14" y="4" width="6" height="6" rx="1"/><rect x="4" y="14" width="6" height="6" rx="1"/><rect x="14" y="14" width="6" height="6" rx="1"/>',
        "nodes": '<circle cx="6" cy="12" r="2"/><circle cx="18" cy="6" r="2"/><circle cx="18" cy="18" r="2"/><path d="m8 11 8-4M8 13l8 4"/>',
        "shield": '<path d="M12 3 20 6v5c0 5-3.4 8.5-8 10-4.6-1.5-8-5-8-10V6l8-3Z"/><path d="m9 12 2 2 4-4"/>',
        "bars": '<path d="M4 19V9m5 10V5m5 14v-7m5 7V7"/>',
    }
    return f'<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{paths.get(name, paths["spark"])}</svg>'


def card(service: dict, index: int) -> str:
    icons = ["grid", "shield", "nodes", "spark", "arrow", "bars"]
    return f"""
    <a class="service-card reveal" href="/services/{service['slug']}/">
      <span class="card-icon">{icon(icons[index])}</span>
      <span class="card-index">0{index + 1} / 06</span>
      <h3>{escape(service['name'])}</h3>
      <p>{escape(service['short'])}</p>
      <span class="card-link">Explore service {icon('arrow')}</span>
    </a>"""


def shell(title: str, description: str, content: str, active: str = "") -> str:
    nav_services = "".join(
        f'<a href="/services/{s["slug"]}/">{escape(s["name"])}</a>' for s in SERVICES
    )
    nav = f"""
    <a class="skip-link" href="#main">Skip to content</a>
    <header class="site-header">
      <div class="container header-inner">
        <a class="brand brand-wordmark" href="/" aria-label="Arixova Tech home"><img src="/assets/arixova-logo.png?v=2" alt="Arixova Tech"></a>
        <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="primary-navigation">
          <span class="sr-only">Open navigation</span><span class="menu-lines"></span>
        </button>
        <nav class="primary-nav" id="primary-navigation" aria-label="Main navigation">
          <a class="nav-link {'is-current' if active == 'home' else ''}" href="/">Home</a>
          <div class="nav-group">
            <a class="nav-link {'is-current' if active == 'services' else ''}" href="/services/">Services</a>
            <div class="nav-dropdown">{nav_services}</div>
          </div>
          <a class="nav-link {'is-current' if active == 'about' else ''}" href="/about/">About</a>
          <a class="nav-link {'is-current' if active == 'contact' else ''}" href="/contact/">Contact</a>
          <a class="button button-small button-blue nav-cta" href="/contact/">Book a consultation {icon('arrow')}</a>
        </nav>
      </div>
    </header>"""
    footer = f"""
    <footer class="site-footer">
      <div class="container footer-main">
        <div class="footer-brand">
          <a class="brand brand-light" href="/" aria-label="Arixova Tech home"><span class="brand-mark"><span>A</span><i>T</i></span><span class="brand-name">arixova<span>tech</span></span></a>
          <p>Thoughtful technology for the way your business works.</p>
          <a class="footer-email" href="mailto:hello@arixova.tech">hello@arixova.tech</a>
        </div>
        <div class="footer-links"><h2>Explore</h2><a href="/about/">About us</a><a href="/services/">Services</a><a href="/contact/">Contact</a></div>
        <div class="footer-links"><h2>Services</h2>{''.join(f'<a href="/services/{s["slug"]}/">{escape(s["name"])}</a>' for s in SERVICES)}</div>
      </div>
      <div class="container footer-bottom"><span>© <span data-year>2026</span> Arixova Tech Ltd</span><div><a href="/privacy/">Privacy</a><a href="/cookies/">Cookies</a></div><span>Built around outcomes.</span></div>
    </footer>
    <script src="/site.js" defer></script>"""
    return f"""<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0f192a">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(title, quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <title>{escape(title)}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Sora:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/site.css?v=2">
</head>
<body>
{nav}
<main id="main">{content}</main>
{footer}
</body>
</html>"""


def write_page(route: str, title: str, description: str, content: str, active: str = "") -> None:
    directory = ROOT / route.strip("/")
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "index.html").write_text(shell(title, description, content, active), encoding="utf-8")


def build() -> None:
    cards = "".join(card(s, i) for i, s in enumerate(SERVICES))
    home = f"""
    <section class="hero">
      <div class="hero-grid" aria-hidden="true"></div>
      <div class="container hero-layout">
        <div class="hero-copy">
          <p class="eyebrow eyebrow-light"><span class="eyebrow-dot"></span> Technology, made useful</p>
          <h1>Better systems.<br><span>Better business.</span></h1>
          <p class="hero-intro">We build the digital tools that help your business move forward — from a sharper website to simpler, smarter ways of working.</p>
          <div class="hero-actions"><a class="button button-blue" href="/contact/">Book a consultation {icon('arrow')}</a><a class="text-link text-link-light" href="/services/">Explore services <span>↘</span></a></div>
          <div class="hero-note"><span class="note-line"></span><span>Practical technology. Thoughtful delivery.</span></div>
        </div>
        <div class="hero-art" aria-label="Abstract illustration of connected digital systems">
          <div class="art-glow"></div><div class="art-orbit orbit-one"></div><div class="art-orbit orbit-two"></div><div class="art-orbit orbit-three"></div>
          <div class="art-core"><div class="core-cross"></div><div class="core-ring"></div><span class="core-label">ARIXOVA<br><small>ENGINEERED FOR PEOPLE</small></span></div>
          <div class="orbit-node node-a">{icon('grid')}</div><div class="orbit-node node-b">{icon('nodes')}</div><div class="orbit-node node-c">{icon('spark')}</div>
          <div class="art-caption"><span>01 — CONNECT</span><span>Ideas into working systems</span></div>
        </div>
      </div>
      <div class="container hero-bottom"><span>UK technology consultancy</span><span class="bottom-rule"></span><span>Web · Systems · Automation</span></div>
    </section>
    <section class="intro-section section-pad">
      <div class="container intro-layout reveal">
        <p class="eyebrow">Good technology should feel clear.</p>
        <div><h2>Built around your work.<br><span class="text-muted">Not the other way round.</span></h2><p class="intro-text">The right digital tools make everyday work easier, help customers move with confidence and give your team room to focus. We bring strategy and engineering together to make that happen.</p></div>
      </div>
    </section>
    <section class="services-section section-pad" id="services">
      <div class="container">
        <div class="section-heading reveal"><div><p class="eyebrow">What we do</p><h2>Six disciplines.<br><span class="text-muted">One clear direction.</span></h2></div><p>Start with one meaningful improvement, or bring the pieces together into a more joined-up digital operation.</p></div>
        <div class="service-grid">{cards}</div>
      </div>
    </section>
    <section class="manifesto section-pad">
      <div class="container manifesto-layout reveal"><div><p class="eyebrow eyebrow-light">The Arixova approach</p><h2>Technology should<br>earn its place.</h2></div><div class="manifesto-copy"><p>We start with the work you need to get done. Then we find a proportionate way to make it easier — with clear decisions, considered engineering and no complexity for its own sake.</p><a class="text-link text-link-light" href="/about/">Get to know us <span>↗</span></a></div><div class="manifesto-lines" aria-hidden="true"><i></i><i></i><i></i><i></i></div></div>
    </section>
    <section class="process-section section-pad">
      <div class="container"><div class="section-heading reveal"><div><p class="eyebrow">How we work</p><h2>Clear from<br><span class="text-muted">the first conversation.</span></h2></div><p>Good work comes from shared understanding. Every engagement has a clear purpose, sensible scope and regular points to review progress.</p></div>
      <ol class="process-list">
        <li class="reveal"><span>01</span><div><h3>Listen</h3><p>We learn how your business works and what needs to change.</p></div>{icon('arrow')}</li>
        <li class="reveal"><span>02</span><div><h3>Shape</h3><p>We agree a practical approach, scope and the questions to resolve.</p></div>{icon('arrow')}</li>
        <li class="reveal"><span>03</span><div><h3>Build</h3><p>We deliver in focused steps, sharing progress and seeking useful feedback.</p></div>{icon('arrow')}</li>
        <li class="reveal"><span>04</span><div><h3>Support</h3><p>We hand over clearly and discuss what ongoing care makes sense.</p></div>{icon('arrow')}</li>
      </ol></div>
    </section>
    <section class="cta-band"><div class="container cta-layout reveal"><div><p class="eyebrow eyebrow-light">A useful first step</p><h2>Let’s find the<br>right next move.</h2></div><div><p>Tell us what is slowing things down or where you see an opportunity. We’ll start with a straightforward conversation.</p><a class="button button-light" href="/contact/">Start a conversation {icon('arrow')}</a></div></div></section>"""
    write_page("", "Arixova Tech | Technology that moves business forward", "A UK technology consultancy building thoughtful websites, digital tools and practical automation around business outcomes.", home, "home")

    service_index = f"""
    <section class="page-hero"><div class="container page-hero-inner"><p class="eyebrow">Our services</p><h1>Technology for<br><span class="text-muted">the work ahead.</span></h1><p class="page-lead">Six practical disciplines to help your business build, connect and improve its digital operation.</p></div></section>
    <section class="services-section section-pad"><div class="container"><div class="service-grid service-grid-page">{cards}</div><div class="center-cta"><p>Not sure where to begin? We can help you find a useful first step.</p><a class="button button-blue" href="/contact/">Talk it through {icon('arrow')}</a></div></div></section>"""
    write_page("services", "Our Services | Arixova Tech Ltd", "Explore website development, website management, custom tools, AI integration, workflow automation and digital strategy.", service_index, "services")

    for service in SERVICES:
        problem_items = "".join(f"<li>{escape(item)}</li>" for item in service["problems"])
        deliver_items = "".join(f"<li>{escape(item)}</li>" for item in service["deliverables"])
        faq_items = "".join(f"<details class=\"faq-item\"><summary>{escape(question)}<span aria-hidden=\"true\">+</span></summary><p>{escape(answer)}</p></details>" for question, answer in service["faqs"])
        content = f"""
        <section class="page-hero service-hero"><div class="container page-hero-inner"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/services/">Services</a><span>/</span><span>{escape(service['name'])}</span></nav><p class="eyebrow">Arixova services / {escape(service['name'])}</p><h1>{escape(service['promise'])}</h1><p class="page-lead">{escape(service['intro'])}</p><a class="button button-blue" href="/contact/?service={service['slug']}">Discuss your project {icon('arrow')}</a></div></section>
        <section class="detail-section section-pad"><div class="container detail-grid"><div><p class="eyebrow">The challenge</p><h2>Does this sound familiar?</h2></div><ul class="check-list">{problem_items}</ul></div></section>
        <section class="detail-section detail-tint section-pad"><div class="container detail-grid"><div><p class="eyebrow">What we deliver</p><h2>Practical work.<br><span class="text-muted">Clearly scoped.</span></h2></div><ul class="deliver-list">{deliver_items}</ul></div></section>
        <section class="detail-section detail-tint section-pad"><div class="container"><div class="section-heading"><div><p class="eyebrow">Illustrative use cases</p><h2>Imagine what<br><span class="text-muted">could work better.</span></h2></div><p>These are examples to make the possibilities concrete, not claims about completed client projects.</p></div><div class="examples-grid">{''.join(f'<article class="example-card"><span class="example-mark">{icon("spark")}</span><p>{escape(example)}</p><small>Illustrative scenario</small></article>' for example in service['examples'])}</div></div></section>
        <section class="detail-section section-pad"><div class="container"><div class="section-heading"><div><p class="eyebrow">How it works</p><h2>A focused path<br><span class="text-muted">from idea to handover.</span></h2></div><p>We agree the scope and checkpoints together. The exact stages depend on the work, but the next step stays clear.</p></div><ol class="service-steps"><li><span>01</span><div><h3>Understand</h3><p>We learn your goals, current setup and constraints.</p></div></li><li><span>02</span><div><h3>Plan</h3><p>We agree the approach, deliverables and practical milestones.</p></div></li><li><span>03</span><div><h3>Deliver</h3><p>We build or make the changes in reviewable steps.</p></div></li><li><span>04</span><div><h3>Handover</h3><p>We explain what is ready, how to use it and what support is agreed.</p></div></li></ol></div></section>
        <section class="detail-section detail-dark section-pad"><div class="container detail-grid"><div><p class="eyebrow eyebrow-light">The outcome</p><h2>Make room<br>for better work.</h2></div><p class="dark-detail-copy">{escape(service['benefit'])}</p></div></section>
        <section class="detail-section section-pad"><div class="container faq-layout"><div><p class="eyebrow">A few useful answers</p><h2>Before we begin.</h2><p>{escape(service['need'])}</p></div><div class="faq-list">{faq_items}</div></div></section>
        <section class="cta-band"><div class="container cta-layout"><div><p class="eyebrow eyebrow-light">Your next step</p><h2>Start with<br>a conversation.</h2></div><div><p>We’ll learn what you need, discuss the options and agree whether there’s a sensible fit.</p><a class="button button-light" href="/contact/?service={service['slug']}">Enquire about {escape(service['name'].lower())} {icon('arrow')}</a></div></div></section>"""
        write_page(f"services/{service['slug']}", f"{service['name']} | Arixova Tech Ltd", service["short"], content, "services")

    about = f"""
    <section class="page-hero"><div class="container page-hero-inner"><p class="eyebrow">About Arixova</p><h1>Good technology<br><span class="text-muted">starts with listening.</span></h1><p class="page-lead">We’re a technology consultancy helping businesses make thoughtful decisions about the digital systems they rely on.</p></div></section>
    <section class="detail-section section-pad"><div class="container about-layout"><div><p class="eyebrow">Our point of view</p><h2>Useful beats complicated.</h2></div><div class="about-copy"><p>Technology is only valuable when it helps people do something better. That is why we begin with the business context: the customers you serve, the work your team does and the change you want to make.</p><p>From there, we bring strategy and engineering together to shape a clear, maintainable solution. We explain trade-offs in plain language and keep the work focused on what matters.</p></div></div></section>
    <section class="manifesto section-pad"><div class="container manifesto-layout"><div><p class="eyebrow eyebrow-light">How we think</p><h2>Clear thinking.<br>Careful building.</h2></div><div class="manifesto-copy"><p>No borrowed playbooks. No technology for technology’s sake. Just considered decisions, straightforward communication and digital work shaped around your business.</p><a class="text-link text-link-light" href="/services/">See what we do <span>↗</span></a></div></div></section>
    <section class="process-section section-pad"><div class="container"><div class="section-heading"><div><p class="eyebrow">What to expect</p><h2>A partner for<br><span class="text-muted">the whole journey.</span></h2></div><p>We keep the conversation open and the next step visible, from early discovery through delivery and handover.</p></div><div class="about-values"><article><span>01</span><h3>Understand first</h3><p>We ask what the business needs before recommending what to build.</p></article><article><span>02</span><h3>Keep it clear</h3><p>Scope, options and trade-offs are explained in language everyone can use.</p></article><article><span>03</span><h3>Build to last</h3><p>We value maintainable work and a handover your team can understand.</p></article></div></div></section>
    <section class="cta-band"><div class="container cta-layout"><div><p class="eyebrow eyebrow-light">Let’s talk</p><h2>What would you<br>like to improve?</h2></div><div><p>Tell us what your business needs next. We’ll help you work out a sensible place to start.</p><a class="button button-light" href="/contact/">Book a consultation {icon('arrow')}</a></div></div></section>"""
    write_page("about", "About Arixova Tech | Practical Digital Consultancy", "Get to know Arixova Tech, a UK technology consultancy focused on clear thinking and practical digital delivery.", about, "about")

    contact = """
    <section class="page-hero contact-hero"><div class="container contact-heading"><div><p class="eyebrow">Get in touch</p><h1>Start a<br><span class="text-muted">conversation.</span></h1><p class="page-lead">Tell us a little about your business and what you’d like to change. We’ll take it from there.</p><a class="contact-email" href="mailto:hello@arixova.tech">hello@arixova.tech</a></div><div class="contact-aside"><span class="aside-icon">↗</span><p>No jargon. No pressure.<br>Just a useful first conversation.</p></div></div></section>
    <section class="contact-form-section section-pad"><div class="container contact-grid"><div class="form-intro"><p class="eyebrow">Your enquiry</p><h2>What can we<br>help with?</h2><p>Share as much or as little as you like. Please avoid including passwords, payment details or other sensitive information.</p><div class="form-note"><span class="note-line"></span><span>Your details are used to respond to this enquiry.</span></div></div>
      <form class="enquiry-form" id="enquiry-form" novalidate>
        <div class="field-row"><label>Full name <span>*</span><input name="name" autocomplete="name" required maxlength="100" placeholder="Your name"></label><label>Work email <span>*</span><input name="email" type="email" autocomplete="email" required maxlength="254" placeholder="you@company.com"></label></div>
        <div class="field-row"><label>Company <small>(optional)</small><input name="company" autocomplete="organization" maxlength="120" placeholder="Company name"></label><label>Service of interest<select name="service"><option value="">Not sure yet — let’s discuss</option>"""
    contact += "".join(f'<option value="{s["slug"]}">{escape(s["name"])}</option>' for s in SERVICES)
    contact += f"""</select></label></div>
        <label>Your message <span>*</span><textarea name="message" rows="5" required minlength="10" maxlength="5000" placeholder="What are you looking to improve?"></textarea></label>
        <label class="honeypot" aria-hidden="true">Leave this field empty<input name="website" tabindex="-1" autocomplete="off"></label>
        <label class="consent-label"><input name="consent" type="checkbox" required><span>I have read the <a href="/privacy/">privacy notice</a> and understand my details will be used to respond to this enquiry.</span></label>
        <p class="form-status" id="form-status" aria-live="polite"></p>
        <button class="button button-blue form-submit" type="submit">Send enquiry {icon('arrow')}</button>
        <p class="form-fallback">If the form is unavailable, email <a href="mailto:hello@arixova.tech">hello@arixova.tech</a>.</p>
      </form></div></section>
      <section class="contact-next section-pad"><div class="container"><p class="eyebrow">What happens next</p><div class="next-steps"><article><span>01</span><h3>We read your note</h3><p>Your enquiry is reviewed by the team.</p></article><article><span>02</span><h3>We get in touch</h3><p>We’ll follow up to understand the context and answer your questions.</p></article><article><span>03</span><h3>We agree a way forward</h3><p>If it makes sense to proceed, we’ll discuss scope, timing and costs before work begins.</p></article></div></div></section>"""
    write_page("contact", "Book a Consultation | Arixova Tech Ltd", "Contact Arixova Tech to discuss website development, digital tools, AI integration, workflow automation or strategy.", contact, "contact")

    privacy = """
    <section class="page-hero"><div class="container page-hero-inner"><p class="eyebrow">Website information</p><h1>Privacy<br><span class="text-muted">notice.</span></h1><p class="page-lead">A plain-language outline of how this website handles information. The business owner should review and complete this draft before publication.</p></div></section>
    <section class="legal-section section-pad"><div class="container legal-copy"><p class="legal-draft">Draft for review — confirm the controller’s registered details, lawful basis, retention periods and contact process before publishing.</p><h2>Information you send us</h2><p>If you use the enquiry form, it asks for your name, email address, optional company, service interest and message. The website sends this information to the configured enquiry mailbox so the team can respond. Do not include passwords, payment information or unnecessary sensitive details.</p><h2>How information is used</h2><p>Enquiry information is used to review and respond to your request and, where relevant, discuss proposed work. The site should only collect information needed for those purposes.</p><h2>Storage and retention</h2><p>Enquiry messages are delivered by email. The business owner must set and document a suitable retention period, access controls and deletion process before launch. This starter site does not include an analytics service or a visitor database.</p><h2>Cookies and similar technologies</h2><p>This site does not intentionally set analytics or advertising cookies. Your browser and hosting provider may create technical logs needed to deliver and protect the site. See the <a href="/cookies/">cookie information</a>.</p><h2>Your rights and questions</h2><p>Privacy rights depend on the circumstances and applicable law. Before publishing, add the verified details of the organisation responsible for this information and a contact route for privacy requests.</p><h2>Review before launch</h2><p>This draft is not legal advice. Confirm the organisation’s identity, lawful basis, email provider, hosting logs, retention schedule and privacy contact with an appropriate adviser.</p></div></section>"""
    write_page("privacy", "Privacy Notice | Arixova Tech Ltd", "Read how the Arixova website handles information submitted through its enquiry form.", privacy)

    cookies = """
    <section class="page-hero"><div class="container page-hero-inner"><p class="eyebrow">Website information</p><h1>Cookie<br><span class="text-muted">information.</span></h1><p class="page-lead">A simple overview of cookies and similar technologies used by this starter website.</p></div></section>
    <section class="legal-section section-pad"><div class="container legal-copy"><h2>What this site uses</h2><p>The site does not include analytics, advertising pixels or third-party tracking tools by default. It does not set a preference cookie.</p><h2>Essential technical storage</h2><p>Your browser may store ordinary technical data, and the hosting provider may keep server logs to deliver and protect the service. Check the chosen host’s behaviour and privacy documentation before launch.</p><h2>External fonts</h2><p>The current design loads fonts from Google Fonts. This makes a request to Google’s font service when a page loads. If you prefer not to make that request, replace the font link with properly licensed, self-hosted font files before publication.</p><h2>Changes</h2><p>If analytics or other non-essential technologies are added later, review the applicable consent requirements and update this page before enabling them.</p></div></section>"""
    write_page("cookies", "Cookie Information | Arixova Tech Ltd", "Information about cookies and external services used by the Arixova website.", cookies)

    sitemap_routes = ["", "about/", "services/"] + [f"services/{s['slug']}/" for s in SERVICES] + ["contact/", "privacy/", "cookies/"]
    base = "https://arixova-digital-studio.lovable.app/"
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{base}{route}</loc></url>\n" for route in sitemap_routes) + "</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: https://arixova-digital-studio.lovable.app/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    build()
