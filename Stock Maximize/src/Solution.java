import java.io.File;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws FileNotFoundException {
		
		File input = new File("test/input00.txt");
		//InputStreamReader input = new InputStreamReader(System.in);

		Scanner scanner = new Scanner(input);

		int numberOfInputs = Integer.parseInt(scanner.nextLine());

		for (int i = 0; i < numberOfInputs; i++) {
			int numberOfDays = Integer.parseInt(scanner.nextLine());
			long stockPriceToday;
			long expense = 0;
			long income = 0;
			boolean isBought = false;
			int boughtItems = 0;

			long[] stockPrices = Arrays.stream(scanner.nextLine().split(" ")).mapToLong(Long::parseLong).toArray();

			long maxPrice = Arrays.stream(stockPrices).max().getAsLong();

			for (int j = 0; j < numberOfDays; j++) {
				stockPriceToday = stockPrices[j];

				if (stockPriceToday < maxPrice) {
					isBought = true;
					boughtItems++;
					expense += stockPriceToday;
				} else {
					if (isBought) {
						income += (stockPriceToday * boughtItems - expense);
						expense = 0;
						boughtItems = 0;
						isBought = false;
					}

					if (j != stockPrices.length - 1) {
						long[] newArray = Arrays.copyOfRange(stockPrices, j + 1, numberOfDays);
						maxPrice = Arrays.stream(newArray).max().getAsLong();
					}
				}
			}

			System.out.println(income);
		}

	}
}
