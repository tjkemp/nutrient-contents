# Analysis on Average Nutrient Contents of Finnish Foods

The goal of this notebook is to do basic analysis on nutrient contents of Finnish foods and food products used in Finland and provide easily reusable template for other analysis. The nutrient content analysis is based on [Fineli](https://fineli.fi/fineli/en/index)'s open database data which includes over 4,000 foods and 55 nutrient factors.

First to get data understanding some visualizations are done: histograms, boxplots and scatterplots, PCA, MDS representations. Pearson’s, Spearman’s rho and Kendall’s tau correlation tables are also calculated.

The following attributes of the collected from original data in pre-processing phase:

1. ENERC	energy (energia, laskennallinen)
2. CHOAVL	carbohydrates (hiilihydraatti imeytyvä)
3. FAT	    fat (rasva)
4. PROT	    protein (proteiini)
5. FIFIBC	fiber (kuitu, kokonais-)
6. STARCH	starch (tärkkelys)
7. SUGAR	sugars (sokerit)
8. FASAT	saturated fat (rasvahapot tyydyttyneet)
9. NACL	    salt (suola)

## The notebook

See [nutrient-contents notebook on Analysis on Average Nutrient Contents of Finnish Foods](https://github.com/tjkemp/nutrient-contents/blob/master/nutrient-contents.ipynb).

## Examples visualizations

![Histogram](https://github.com/tjkemp/nutrient-contents/blob/master/images/histograms.png)

![Scatter plot](https://github.com/tjkemp/nutrient-contents/blob/master/images/scatterplots.png)

![Principal Component Analysis](https://github.com/tjkemp/nutrient-contents/blob/master/images/pca.png)

![Parallel Coordinates](https://github.com/tjkemp/nutrient-contents/blob/master/images/parallel_coordinates.png)

## Licences

- [MIT License](LICENSE) for the code.
- Data by National Institute for Health and Welfare of Finland, Fineli (22.11.2015). Licence: [Creative Commons Attribution 4.0 (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.en). [Link to data](https://fineli.fi/fineli/en/ohje/19).

## Author

- [tjkemp](https://github.com/tjkemp)
