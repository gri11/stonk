# Stock Prediction Project

## Plan
  - Baselines
    - LSTM
    - GRU
    - ResNLS
  - Hyperparameter tuning
  - Increase layers
  - Increase features

  - if ton: change dataset
    - Stock Mixer

- New ideas
  - Apply Transformers
- Implement ideas
  - TBD
- Experiment
  - Try different features and analysis
- Result analysis
  - Stock Mixer
  - ...baselines
  - ...new ideas


## To-Do List

### Progress 1 Simple Baseline
- [ ] Setup experiments (data, metrics, tools)
   - [ ] choose metrics
- [ ] Run baselines
  - [ ] write more metrics (3)
  - [ ] LSTM GRU (S&P500)
  - [ ] write model ResNLS (1)

## Problem Setup

### Dataset

#### LSTM GRU ResNLS
|                    | S&P500   |
| ------------------ | -------- |
| Start Time (Y-M-D) | 04-08-19 |
| End Time           | 19-10-03 |
| Train Days         | 3366     |
| Val Days           | 251      |
| Test Days          | 191      |

#### StockMixer
|            | S&P500   |
| ---------- | -------- |
| Start Time | 16-01-04 |
| End Time   | 22-05-25 |
| Train Days | 1006     |
| Val Days   | 253      |
| Test Days  | 352      |

### Metric
- Information Coeffcient (IC)
- Rank Information Coeffcient (RIC)
- Precision@N (prec@N)
- Sharpe Ratio (SR)


## Method

### Simple Baseline

$ X \in \mathbb{R}^{T \times F} \to p \in \mathbb{R} \to r \in \mathbb{R} $

$ T = 16, F = 5 $

$ r^{t} = \frac{p^{t} - p^{t-1}}{p^{t-1}}$

$ L = L_\text{MSE} + \alpha \sum_{i=1}^{N} \sum_{j=1}^{N} \max\left(0, -(\hat{r}_{{t}_{i}} - \hat{r}_{{{t}_{j}}})({r}_{{t}_{i}} - {r}_{{{t}_{j}}})\right) $


## Result
| model  |    MAPE |    MASE |      RMSE |   SMAPE |       MAE | sharp_ratio | Directional Accuracy |
| :----- | ------: | ------: | --------: | ------: | --------: | ----------: | -------------------: |
| gru    | 2.51945 | 2.60299 |  0.103868 | 2.56355 | 0.0842575 |    0.411069 |              69.4737 |
| lstm   | 1.68196 | 1.72826 | 0.0750012 | 1.69879 | 0.0560689 |    0.188782 |              67.8947 |
| resnls | 1.77126 |  1.4714 | 0.0769175 | 1.79153 | 0.0590094 |    0.228892 |              70.5263 |

## Reference
- [StockMixer](https://ojs.aaai.org/index.php/AAAI/article/view/28681)
- [ResNLS](https://arxiv.org/abs/2312.01020)
- [MASTER](https://arxiv.org/abs/2312.15235)

## Acknowledgement
- https://github.com/Waterkin/stock-top-papers - for providing the list of top papers in stock prediction


## Future Work
- [MoE Timeseries](https://opensource.salesforce.com/Merlion/v1.1.0/examples/advanced/2_MoE_Forecasting_tutorial.html)
