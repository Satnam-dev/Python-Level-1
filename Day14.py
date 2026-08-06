# Too create chatBot 
# Pre requisite:- Model Id , User Prompt , system prompt ,Groq Api key , MongoB URL

# Src > Controller > groqController.js 
# Controller Folder:- Handle incoming requests from the user

# User Request (Input message submitted by the user to the AI model)
# Get Prompt (The controller extracts the user's message from the request body)
# Validate Prompt (Check whether the prompt exists and is valid)
# Call Service (After validation, the controller sends the prompt to the service)
# Return Service (service returns the AI answer)


# 1.        User Request
#           ↓
# 2.        Get User Prompt(const userPrompt = req.body.prompt;)
#           ↓
# 3.        Validate User Prompt
#           ↓
# 4.        Call Service
#           ↓
# 5.        Return Response

# Src > Controller > groqController.js 
# In the start ,where we import all prompts
# import { bankingPrompt, hospitalityPrompt, insurancePrompt, realEstatePrompt, retailPrompt, travelPrompt } from "../Repository/systemPrompt.js";
# const userPrompt = req.body.prompt; 
# await response.save(); (used to store response in database)



#  Src > Repository > systemPrompt.js
#  Services:- Contains the application's business logic.
#  User Prompt (The service receives the user's prompt from the controller)
#  System Prompt (The service adds a system prompt to guide the AI's response)
#  Update prompt (Instruction given to an AI to modify ,improve or change existing content).
#  The higher the quality of the system prompt, the better the output.
#  Model Selection (The service selects the appropriate AI model to use)
#  Model ID
#  const model = "llama-3.3-70b-versatile";
#  API Call (The service calls the OpenAI API with the combined prompt and model)
#  Stream Processing (AI response is sent to you piece by piece instead of waiting for the full answer at once.)
#  Chunk:- A chunk is a small piece of data received from the stream.
#  It's is used to filter the data and remove the the unwanted data
#  Console Log:- Console logging is used for debugging and monitoring application behavior during execution
#  Token are used to limit the request :- max_tokens: 8192

# 1.        Recieve Validated prompt (user prompt after validation)
#           ↓
# 2.        Get/Add System Prompt
#           ↓
# 3.        Select Model Id
#           ↓
# 4.        Call OpenAI API 
#           ↓
# 5.        Process stream and chunks
#           ↓
# 6.        Build final respose 
#           ↓
# 7.        Build final respose 




# Step to run backend :- cd backend
# npm i 
# npm run dev

# Step to run frontend :- cd frontend
# npm i 
# npm run dev
