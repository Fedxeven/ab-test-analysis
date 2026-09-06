# A/B Test Analysis
Simple A/B test analysis using Python.

## About the project
I analyzed a synthetic A/B test to compare conversion rates between two versions of a product.
- Group A — old version
- Group B — new version

## Results
- Group A conversion: 10%
- Group B conversion: 25%
- P-value: 0.0085

The difference between the groups is statistically significant at the 5% level.

## Conclusion
The new version performed better than the old version in this synthetic experiment.

The result is statistically significant, so the difference is unlikely to be explained by random variation alone.

## Tools
- Python
- pandas
- scipy

## Files
- `data.csv` — experiment data
- `analysis.py` — A/B test analysis
