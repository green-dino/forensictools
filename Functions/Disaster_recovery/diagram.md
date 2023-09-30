```mermaid
graph LR
subgraph CloudApps
    Slack[[Slack]] -->|Critical| Backups
end
subgraph OnPremApps
    Application[[Application]] -->|Non-Critical| Backups
end

style CloudApps fill:#e2f0d9,stroke:#6db84f
style OnPremApps fill:#fce4a4,stroke:#ffa726
```