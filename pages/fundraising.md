---
layout: default
title: "Fundraising"
raised: 1240
goal: 2000
original_url: "/fundraising"
permalink: /fundraising/
---

We want to express our deepest gratitude for the overwhelming support and generosity that you have shown to our organization. Your contributions have helped us make it possible for us to continue our mission of improving the lives of those in our community. We would like to extend our sincere thanks to each and every one of you for your generosity and for your belief in our mission. Your support is truly appreciated, and we could not have done it without you.

We are thrilled to announce that thanks to your generosity, we have raised a total of **$1,240.** This is a testament to the support of our community and the impact that we can make together. We are humbled by the outpouring of support that we have received and are excited to use these funds to continue our mission of improving the lives of those in our community.

# Fundraising

<div class="thermo" data-raised="{{ page.raised }}" data-goal="{{ page.goal }}">
  <div class="thermo-bar" role="img" aria-label="Fundraising progress">
    <div class="thermo-fill"></div>
  </div>
  <div class="thermo-stats">
    <span class="thermo-amount">Raised: ${{ page.raised }}</span>
    <span class="thermo-goal">Goal: ${{ page.goal }}</span>
    <span class="thermo-percent" aria-live="polite"></span>
  </div>
</div>

<script>
(function() {
  const el = document.querySelector('.thermo');
  if (!el) return;
  const raised = parseFloat(el.dataset.raised) || 0;
  const goal = parseFloat(el.dataset.goal) || 1;
  const pct = Math.min(100, Math.round((raised / goal) * 100));
  const fill = el.querySelector('.thermo-fill');
  const pctEl = el.querySelector('.thermo-percent');
  fill.style.width = pct + '%';
  fill.setAttribute('aria-valuenow', pct);
  pctEl.textContent = pct + '% of goal';
})();
</script>
