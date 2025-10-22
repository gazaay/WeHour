# WeHour Documentation

This repository contains the WeHour documentation site built with Docsify.

## 🚀 Quick Start

### Local Development
```bash
# Start local server
cd docs
python3 -m http.server 3001
```

Visit: http://localhost:3001

### Netlify Deployment

This site is configured for automatic deployment to Netlify.

**Deployment Settings:**
- **Build Command**: `echo 'Static site - no build needed'`
- **Publish Directory**: `docs`
- **Node Version**: 18

## 📁 Project Structure

```
WeHour/
├── docs/                    # Documentation files
│   ├── index.html          # Main Docsify configuration
│   ├── _sidebar.md         # Navigation sidebar
│   ├── README.md           # Homepage content
│   ├── core-concepts/      # Core concept documentation
│   ├── tokenomics/         # Tokenomics documentation
│   ├── technical-architecture/ # Technical documentation
│   ├── business-model/     # Business model documentation
│   ├── implementation/     # Implementation guides
│   └── resources/          # Additional resources
├── netlify.toml            # Netlify configuration
└── package.json           # Node.js dependencies
```

## 🎨 Features

- **Light Theme**: Clean, professional light grey background
- **Mermaid Diagrams**: Interactive flowcharts and diagrams
- **Search**: Full-text search across all documentation
- **Responsive**: Mobile-friendly design
- **Navigation**: Clean sidebar navigation
- **Brand Colors**: WeHour pink accent colors throughout

## 🔧 Configuration

The site uses Docsify with the following plugins:
- Search functionality
- Image zoom
- Code copying
- Pagination
- Mermaid diagram rendering

## 📝 Content

The documentation covers:
- **Core Concepts**: Vision, mission, problem statement, solution overview
- **Tokenomics**: Dual token model, VH$ and VB$ tokens, economic models
- **Technical Architecture**: Blockchain infrastructure, smart contracts, security
- **Business Model**: Revenue streams, cross-merchant model, competitive analysis
- **Implementation**: Roadmap, partnerships, pilot programs, risk management
- **Resources**: FAQ, glossary, references, contact information

## 🌐 Deployment

This site is automatically deployed to Netlify when changes are pushed to the main branch.

**Live Site**: [Your Netlify URL will appear here after deployment]
