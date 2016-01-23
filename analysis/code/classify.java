import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;

import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.sentiment.SentimentCoreAnnotations;
import edu.stanford.nlp.util.CoreMap;

public class classify {
	public static void main(String[] args) throws IOException {

		Properties props = new Properties();
		props.setProperty("annotators", "tokenize, ssplit, pos, lemma, parse, sentiment");
		props.setProperty("sentiment.model", "/Users/Doctor_Einstein/Documents/stockMartket/analysis/nlp/stanford/stockTwits2.ser.gz");
		StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

		FileInputStream fis = new FileInputStream("/Users/Doctor_Einstein/Documents/stockMartket/analysis/data/justTweets.txt");
		BufferedReader br = new BufferedReader(new InputStreamReader(fis));

		String line = null;
		while ((line = br.readLine()) != null) {
			Annotation annotation = pipeline.process(line);
			List<CoreMap> sentences = annotation.get(CoreAnnotations.SentencesAnnotation.class);
			int avg=0; int numSent=0;
			for (CoreMap sentence : sentences) {
				String sentiment = sentence.get(SentimentCoreAnnotations.SentimentClass.class);
				int sentimentValue = 0;
				switch (sentiment) {
				case "Very positive":
					sentimentValue = 1;
					break;
				case "Positive":
					sentimentValue = 1;
					break;
				case "Neutral":
					sentimentValue = 0;
					break;
				case "Negative":
					sentimentValue = -1;
					break;
				case "Very negative":
					sentimentValue = -1;
					break;
				}
				avg += sentimentValue; numSent ++;
			}
			avg = (int) Math.round( (double) avg / (double) numSent); // composite sentiment
			System.out.println(avg);
		}

		br.close();
	}
}
