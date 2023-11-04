# AI-Security-DragonGPT

![DragonGPT](./img/logo.png)

## Introductions
This challenge will show you how AI can be used for automatic threat modelling analysis.
It should also give you more insights of limits and the difference between human and AI threat models.

### Tasks
* Identify threats based on provided threat model
* Use AI for automatic threat modelling
* Answer the questions in the write-up

### Artifacts
* Docker proxy for communicating with OpenAI API
* Python script for automatic threat modelling

### Architecture
````bash
+------------------+                    +------------------+                   +------------------+
|                  |                    |                  |                   |                  |
|                  |                    |                  |                   |                  |
|                  |                    |                  |                   |                  |
|    HL Internet   <--------------------|    OpenAI Key    <-------------------|     DragonGPT    |
|    Proxy         |                    |    Injector      |                   |                  |
|                  |                    |                  |                   |                  |
|                  |                    |                  |                   |                  |
+------------------+                    +------------------+                   +------------------+
````

### Step 1: Clone Repository
Clone the repository, which contains the python script and the example diagram.
```
git clone https://gitlab.ost.ch/sa2/chatgpt-3-security-lab.git
```

### Step 2: Import model
Import the provided threat model to Threat Dragon.
Model: `diagrams/example/basic_scenario.json`
1. Install Threat Dragon if haven't already. https://threatdragon.github.io/install/
2. Choose `Open an existing model`
3. Copy & Paste the JSON code provided from the repo
4. Select `Import`

### Step 3: Add threats
Now add the threats to the properties according to the STRIDE methodology.

### Step 4: Threat modelling with AI
Now we come to the interesting part, where we let AI do our job. \
The provided python script `main.py` will analyse the threat model and give you a list of possible threats.

First you need to start the `dragon-gpt3-proxy` ressource by just clicking the play button. \
This will give you a `FQDN` which is needed as an argument for the script later.

````
# Install deps
$ pip install -r requirements.txt

# Run script
python3 main.py  --proxy https://<FQDN>/endpoint diagrams/example/basic_scenario.json

#Example
python3 main.py  --proxy https://8c261beb-99bc-42bc-b7d7-dfa8e9a26e34.idocker.vuln.land/endpoint diagrams/example/basic_scenario.json
````
There will be a command line output of the result but also a `output.txt` file with the same content as the cli output. \
Feel free to get a deeper understanding of the script by looking at the python code.

### Solution
Please submit your answer to the security questions below in a write-up

### Security Questions
* What were the advantages of conducting a threat analysis by hand? Were there any limitations or challenges associated with this approach?
* What were the advantages of using AI for threat analysis? Were there any limitations or challenges with the AI approach?
* Did the manual analysis identify any threats that the AI-based analysis missed, or vice versa? If so, please provide examples.
* How might you improve or combine both methods to enhance threat analysis in the future?

