import argparse
import os
from dotenv import load_dotenv
from utils.diagram import DiagramHandler
from utils.chatgpt import OpenAIHandler


def handle_arguments():
    parser = argparse.ArgumentParser(description=
                                     "Dragon-GPT is a CLI program that makes an automatic threat analysis "
                                     "using Chat-GPT on a given scenario produced using OWASP Threat Dragon.")
    parser.add_argument("filename", help="Path to the diagram (json format expected)")
    parser.add_argument("--output", "-o", default="output.txt", help="Export the response from OpenAI to a txt file")
    parser.add_argument("--proxy", "-p", help="Proxy to use")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = handle_arguments()
    diagram = DiagramHandler(args.filename)
    sentence = diagram.make_sentence()
    load_dotenv()
    env_proxy = os.getenv("PROXY")
    if args.proxy:
        proxy = args.proxy
    else:
        if env_proxy == "":
            print("Please specify a proxy to process the request.")
            exit()
        else:
            proxy = env_proxy
    print(sentence)
    chatgpt = OpenAIHandler(args.output, proxy)
    response = chatgpt.do_threat_modeling(sentence)

    for comp in diagram.components:
        if comp["type"] == DiagramHandler.flow_type:
            for flow in comp["flow"]:
                if "preventive_measures" in flow:
                    response += f"\nPreventive measures for {flow['name']}: {flow['preventive_measures']}"
