import matplotlib.pyplot as plt

# =============================================================
# PMTCT Community-Level Analysis
# Data Source: PEPFAR MER Dataset
# Analysis by: Obiageli Iweanoge | WARPD Fellow 2026
# =============================================================


# -------------------------------------------------------------
# Figure 1: HIV Testing Coverage Across LGAs
# Question: How does HIV testing coverage vary across LGAs?
# -------------------------------------------------------------

testing = clean_df[['PMTCT_STAT']].sort_values('PMTCT_STAT', ascending=False).reset_index(drop=True)

plt.figure(figsize=(10, 5))
plt.bar(range(len(testing)), testing['PMTCT_STAT'])
plt.title('How HIV testing coverage varies across LGAs')
plt.xlabel('LGAs')
plt.ylabel('Number of Pregnant Women Tested')
plt.savefig('fig1-hiv-testing-coverage.png', dpi=300, bbox_inches='tight')
plt.show()


# -------------------------------------------------------------
# Figure 2: HIV Positive Cases Distribution Across LGAs
# Question: Where are HIV positive cases most concentrated?
# -------------------------------------------------------------

positivity = clean_df[['PMTCT_STAT_POS']].sort_values('PMTCT_STAT_POS', ascending=False).reset_index(drop=True)

plt.figure(figsize=(10, 5))
plt.bar(range(len(positivity)), positivity['PMTCT_STAT_POS'])
plt.title('How Are HIV Positive Cases Distributed Along LGAs?')
plt.xlabel('Ranked LGAs')
plt.ylabel('Number of Positive Cases')
plt.savefig('fig2-hiv-positive-distribution.png', dpi=300, bbox_inches='tight')
plt.show()


# -------------------------------------------------------------
# Figure 3a: ART Coverage Across LGAs
# Question: What proportion of HIV positive pregnant women receive ART?
# -------------------------------------------------------------

art = clean_df[['PMTCT_STAT_POS', 'PMTCT_ART']].copy()
art['ART_Coverage'] = art['PMTCT_ART'] / art['PMTCT_STAT_POS']
art = art.fillna(0)

art_sorted = art[['ART_Coverage']].sort_values('ART_Coverage', ascending=False).reset_index(drop=True)

plt.figure(figsize=(10, 5))
plt.bar(range(len(art_sorted)), art_sorted['ART_Coverage'])
plt.title('Proportion of HIV positive pregnant women receiving ART across LGAs')
plt.xlabel('LGAs')
plt.ylabel('ART Coverage (Proportion)')
plt.savefig('fig3a-art-coverage.png', dpi=300, bbox_inches='tight')
plt.show()


# -------------------------------------------------------------
# Figure 3b: PMTCT Cascade Across LGAs
# Question: How does the PMTCT cascade differ across LGAs?
# -------------------------------------------------------------

cascade = clean_df[['PMTCT_STAT', 'PMTCT_STAT_POS', 'PMTCT_ART']].copy()
cascade = cascade.sort_values('PMTCT_STAT', ascending=False).reset_index(drop=True)

top10 = cascade.head(10)
top10.plot(kind='bar', figsize=(12, 6))
plt.title('How PMTCT cascade differ across LGAs')
plt.ylabel('Number of Pregnant Women')
plt.savefig('fig3b-pmtct-cascade.png', dpi=300, bbox_inches='tight')
plt.show()


# -------------------------------------------------------------
# Figure 4: Patterns of Disparity Across LGAs
# Question: What patterns of disparity exist across LGAs?
# -------------------------------------------------------------

disparity = clean_df[['PMTCT_STAT', 'PMTCT_STAT_POS', 'PMTCT_ART']].copy()
disparity['ART_Coverage'] = disparity['PMTCT_ART'] / disparity['PMTCT_STAT_POS']
disparity = disparity.fillna(0)

# Normalize for comparison across variables
disparity_norm = (disparity - disparity.min()) / (disparity.max() - disparity.min())

plt.figure(figsize=(10, 5))
plt.plot(disparity_norm['PMTCT_STAT'], label='Testing')
plt.plot(disparity_norm['PMTCT_STAT_POS'], label='Positive')
plt.plot(disparity_norm['PMTCT_ART'], label='ART')
plt.plot(disparity_norm['ART_Coverage'], label='ART Coverage')
plt.title('Patterns of disparity that exist across LGAs')
plt.xlabel('LGAs')
plt.ylabel('Normalized Values')
plt.legend()
plt.savefig('fig4-disparity-patterns.png', dpi=300, bbox_inches='tight')
plt.show()
