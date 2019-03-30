from allennlp.predictors.predictor import Predictor
predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/decomposable-attention-elmo-2018.02.19.tar.gz")

class Query:

    def ask_question(self,text,question):
        predict = predictor.predict(passage=text,question=question)
        return predict['best_span_str']


    def check_hypothesis(self,text,hypothseis):
        predict = predictor.predict(hypothesis= text,premise=hypothseis)
        return predict['label_probs']

    print(ask_question("Marijuana is legal in Thailand and India","Marijuana is legal in which countries"))
