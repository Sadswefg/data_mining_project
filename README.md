Cryptocurrency price predictions using 
sentiment analysis – Final Report 
VinUniversity 
Course: Data Mining & Big Data Analytics 
Instructor: Professor Khoa Doan 
Vu Nguyen (V202000145) 
Github: Sadswefg/data_mining_project (github.com) 
1. Introduction 
a. Problem statement 
Nowadays, with a fast-paced world of cryptocurrencies, market dynamics are heavily 
influenced by a mix between traditional financial indicators and the powerful swings of 
public sentiment. The inherently unstable nature of cryptocurrency prices means they 
react strongly to the collective emotions and viewpoints shared across different media 
channels. This complex relationship between market performance and public 
conversation offers a unique set of challenges and opportunities for investors and analysts 
dedicated to refining their price movement predictions. 
Hence, predicting price trends specifically related to cryptocurrency is an extremely 
difficult task because of various factors. Moreover, typical classification models for 
financial analysis usually fail to capture all the influences, especially those rooted in public 
sentiment. This shortfall can lead to an occlusion in capturing the whole context in the 
price analysis. Therefore, given the critical role that investors sentiment plays in 
influencing market dynamics, there is a persuasive need for models that incorporate with 
the sentiment. This approach promises to improve predictive accuracy among the existing 
methods. Consequently, this project aims to create a sophisticated predictive model that 
uses public sentiment to forecast the price movement more precisely. 
b. Advantages of using sentiment analysis 
The main factor that drives the price of cryptocurrencies is obviously the investors. Thus, 
using sentiment analysis serves as a powerful tool to capture public opinion and emotional 
responses, which plays a pivotal role in shaping the domain. The following underscore the 
advantages of integrating sentiment analysis to the price predictive model: 
• Captures public opinion and emotional responses. 
• Influences market dynamics significantly. 
• Immediate response to news. 
• Enhances the accuracy of classification models. 
By addressing these aspects, this project aims to build a more robust model for 
cryptocurrency price prediction, enhancing accuracy through the integration of sentiment 
analysis. This approach not only aligns with current technological advancements in data 
analytics but also caters to the unique characteristics of the cryptocurrency market. 
2. Related work & Proposed method and experiment 
a. Related works 
There has been excessive research on predictive price models using sentiment analysis. 
However, this project would focus solely on these following papers: 
• The conference paper “Cryptocurrency price prediction using Twitter sentiment 
analysis” (Haritha & Sahana, 2023) suggests using GRU model to predict the price 
because of its ability to handle the vanishing gradient problem from using RNNs 
methods. Also, the authors use a fine-tuned BERT model to predict the sentiment 
because they believed that using transformer encoder such as BERT would be best 
to tackle the NLP problems, specifically in the financial domain. Additionally, 
VADER was used as explained in the text due to its belief that it is outperforming 
human raters. The evaluation metric used in the paper was MAPE (Mean absolute 
percentage error) which illustrates the difference between the predicted and actual 
data. The paper achieved an average of 9.45% MAPE for sentiment prediction using 
finBERT and 3.6% MAPE for the price prediction (Bitcoin price). 
Figure 1: Result comparison between Bi-LSTM, GRU for price prediction and result of 
FinBeRT. 
• In “A deep learning-based cryptocurrency price prediction scheme for financial 
institutions” (Patel, Tanwar, Gupta, & Kumar, 2020) suggested that using a 
combination of LSTM and GRU model returned a best result. Notice that this paper 
only focuses on price prediction but not using the sentiment analysis as a feature in 
their model.  
Figure 2: LSTM vs LSTM + GRU for price prediction 
b. Proposed method & experiment 
With the aforementioned related works, the approach adopted in this project involves 
integrating sentiment data with a combined LSTM and GRU model. This method aims to 
capture both short-term and long-term dependencies in the data, leveraging the strengths 
of each model type. In addition to the model integration, this project focuses on several 
key techniques to enhance prediction accuracy: 
• Objective: Create a predictive model that uses public sentiment to forecast price 
movements more precisely. 
• Baseline: The combination of LSTM and GRU models with sentiment analysis as 
part of the input features. 
• Proposed method & experiment: applying model’s enhancement methods such as: 
o Ensemble: Training the LSTM and GRU model separately, then, compute the 
average output from both models as the prediction. 
o Normalization: using MinMaxScaler to ensure that all input data are on a 
similar scale to improve model performance. 
o Hyperparameter Tuning: Systematically adjusting model parameters to find 
the optimal configuration. 
o Outlier Detection and Handling: Using the z-score method to identify and 
manage outliers, ensuring they do not adversely affect model training and 
predictions. 
• Performance benchmarking: compare outputs from proposed approaches with the 
baseline model. 
These methods collectively aim to address the challenges of predicting cryptocurrency 
prices in a highly volatile market, providing a more reliable and accurate forecasting tool. 
c. Dataset 
The dataset used in this project is composed of: 
• Bitcoin Price Data: 
o Source: investing.com 
o Coverage: Daily records from 2012 to 2024 
o Features: Price, Open, High, Low, Volume, Change %, day_of_year, score 
(aggregated sentiment score) 
o Train dataset: records from 2012 to 2023. 
o Test dataset: records from the start of 2024 to June 16th, 2024. 
• Sentiment Data: 
o Source: investing.com forums, Reddit headlines & Kaggle's dataset (only 
extract the sentiment score column then combine it with the actual data). 
o Preprocessing: Label sentiment using VADERs sentiment analysis tool. 
d. Evaluation metrics 
To give a “fair and square” comparison with the above papers and my experiments, I will 
use MAE, MSE, MAPE and RMSE to evaluate the proposed scheme. 
• 𝑀𝑆𝐸= 1
 𝑁
 • 𝑀𝐴𝐸=1
 𝑁
 • 𝑀𝐴𝑃𝐸=1
 𝑁
 𝑁
 𝑖 =1 
∑ (𝑌𝑖 −𝑌𝑖
 ′)2
 𝑁
 𝑖 =1 
∑ |𝑌𝑖 −𝑌𝑖
 ′|
 𝑁
 ∑ |𝑌𝑖−𝑌𝑖
 ′
 𝑖 =1 
• 𝑅𝑀𝑆𝐸=√𝑀𝑆𝐸
 𝑌𝑖
 |
 Where Yi is the actual data, Y’i is the predicted data and n is the number of observations. 
Additionally, line plots will also be implemented for a quick visual comparison between 
models. 
3. Detailed implementation & Evaluation 
a. Implementation 
The project’s models are implemented using Pytorch. For the data preprocessing stage, I 
handle the missing values due to the resource limitation with forward and backward fill. 
Then, I initialize the MinMaxScaler to normalize the data into a format, specifically one hot, 
so that the model can capture the data context faster. The models are later trained using 
the Adam optimizer with Mean Squared Error as the loss function. To keep the benchmark 
be fair and square, the setting of models in this project are keeping as the same: 
• LSTM/GRU: 1 layer, 50 hidden units, batch first. 
• Adding Linear Layer to map to output since this project is a regression task. 
• Adding Dropout Layer with p = 0.2 to avoid overfitting. 
• Models are trained with 50 epochs, batch size of 32 and learning rate of 0.0001. 
The z-scores is implemented to detect the outlier by finding those data points that are 
further away (z-score > 3) from the standard deviation. 
Figure 3: Outliers detection function – Code snippet. 
From figure 3, `stats.zscore(df[features])` is used to compute the z-score following the 
formula: 𝑧 = (𝑋 − 𝜇)
 𝜎
 where X is the actual value, 𝜇 is the mean of the column and 𝜎 is the 
standard deviation of the column. Then, using a Boolean mask identifying rows where any 
feature’s z-score is greater than 3 (a common threshold for outlier detection). 
Figure 4: Detected and removed outliers. 
b. Evaluation 
Baseline model: Combination of LSTM & GRU model. 
• Evaluation: RMSE: 2222.8131, MSE: 4940898.0797, MAPE: 0.0289 
Figure 5: Combination of LSTM & GRU price prediction. 
Ensemble method: Training LSTM & GRU model separately and averaging the predictions 
from both models. 
• Evaluation: RMSE: 1826.4708, MSE: 3335995.5305, MAPE: 0.0235 
Figure 6: Ensemble method (LSTM & GRU) price prediction. 
Ensemble + Handling outliers: Using model from the above ensemble method after 
removing outliers within the input features. 
• Evaluation: RMSE: 1237.1108, MSE: 1530443.2515, MAPE: 0.0134 
Figure 7: Ensemble method with outlier detection. 
4. Conclusion 
This project illustrates how integrating sentiment analysis with traditional financial models 
could enhance the accuracy of cryptocurrency price predictions. While the volatile nature 
of cryptocurrency markets posed significant challenges to the domain, this project 
addresses those challenges through an ensemble method combining with LSTM and GRU 
models. Additionally, techniques such as normalization, hyperparameter tuning, and 
outlier detection using z-score method further enhanced the performance of the proposed 
approach where they reduced the evaluation metrics like RMSE, MSE, and MAPE with a 
noticeable amount comparing to the baseline model. The results showed that integrating 
sentiment data and employing the proposed method suggested a more accurate and 
reliable tool for predicting cryptocurrency prices. 
5. Reference 
• Patel, M. M., Tanwar, S., Gupta, R., & Kumar, N. (2020). A deep learning-based 
cryptocurrency price prediction scheme for financial institutions. Journal of 
Information Security and Applications, 55(102583). 
https://doi.org/10.1016/j.jisa.2020.102583 
• Haritha, G. B., & Sahana, N. B. (2023). Cryptocurrency price prediction using Twitter 
sentiment analysis. In D. C. Wyld et al. (Eds.), Proceedings of the NIAI, MoWiN, 
AIAP, SIGML, CNSA, ICCIoT - 2023 (pp. 13-22). CS & IT - CSCP 2023. 
https://doi.org/10.5121/csit.2023.130302 
• https://www.kaggle.com/code/codeblogger/bitcoin-sentiment-analysis/ 
