import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URI;
import java.util.Scanner;

public class GeminiImageGenerator {
    private static final String API_KEY = System.getenv("GEMINI_API_KEY");
    private static final String ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-preview-image-generation:generateContent";

    public static void main(String[] args) throws Exception {
        String prompt;
        
        // Get prompt from command line arguments or user input
        if (args.length > 0) {
            // Use the first command line argument as the prompt
            prompt = args[0];
        } else {
            // Prompt user to enter a description
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter your image description: ");
            prompt = scanner.nextLine();
            scanner.close();
        }
        
        System.out.println("Generating image for: " + prompt);
        
        String payload = "{\n" +
                "  \"contents\": [{\n" +
                "    \"parts\": [\n" +
                "      {\"text\": \"" + prompt + "\"}\n" +
                "    ]\n" +
                "  }],\n" +
                "  \"generationConfig\": {\"responseModalities\": [\"TEXT\", \"IMAGE\"]}\n" +
                "}";

        URL url = URI.create(ENDPOINT + "?key=" + API_KEY).toURL();
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setDoOutput(true);

        try (OutputStream os = conn.getOutputStream()) {
            os.write(payload.getBytes());
        }

        StringBuilder response = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()))) {
            String line;
            while ((line = br.readLine()) != null) {
                response.append(line);
            }
        }

        // Extract base64 image data from the response (simple parsing)
        String responseStr = response.toString();
        int dataIdx = responseStr.indexOf("\"data\": \"");
        if (dataIdx != -1) {
            int start = dataIdx + 9;
            int end = responseStr.indexOf("\"", start);
            String base64Image = responseStr.substring(start, end);

            // Just print the base64 data to stdout (no file saving)
            System.out.println(base64Image);
        } else {
            System.err.println("No image data found in response.");
            System.exit(1);
        }
    }
}
