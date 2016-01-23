import edu.ucla.sspace.common.StaticSemanticSpace;
import edu.ucla.sspace.common.DocumentVectorBuilder;
import edu.ucla.sspace.common.SemanticSpace;
import edu.ucla.sspace.common.SemanticSpaceIO;

import edu.ucla.sspace.vector.DoubleVector;
import edu.ucla.sspace.vector.DenseVector;
import edu.ucla.sspace.vector.Vector;

import java.io.InputStream;
import java.io.ByteArrayInputStream;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

public class tweetsToRIVectors {
	public static void main(String[] args) throws IOException {

		// get test data and learned semantic representations, respectively
		FileInputStream fis = new FileInputStream("/Users/Doctor_Einstein/Documents/stockMartket/analysis/data/testTweets.txt");
		BufferedReader br = new BufferedReader(new InputStreamReader(fis));

		SemanticSpace sspace = SemanticSpaceIO.load("/Users/Doctor_Einstein/Documents/stockMartket/analysis/data/stockTwitsTrain.sspace");
		int numDims = sspace.getVectorLength();

		// use semantic space to generate (sumnative) representations of documents
		DocumentVectorBuilder builder = new DocumentVectorBuilder(sspace);

		// instantiate empty vector
		DoubleVector documentVector = new DenseVector(numDims);

		String tweet = null;
		while ((tweet = br.readLine()) != null) {
			// convert string to buffered reader
			InputStream is = new ByteArrayInputStream(tweet.getBytes());
			BufferedReader tweetBR = new BufferedReader(new InputStreamReader(is));


			builder.buildVector(tweetBR, documentVector);
			for (double element : documentVector.toArray()) {
				System.out.print(element + ",");
			}
			System.out.println();
		}
	 
		br.close();
	}
}
