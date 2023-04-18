import sys

from google.cloud import language_v1
import six


def sentiment_analysis(content):

    client = language_v1.LanguageServiceClient()
    #content = 'Type any string here.'
    if isinstance(content, six.binary_type):
        content = content.decode("utf-8")

    type_ = language_v1.Document.Type.PLAIN_TEXT
    document = {"type_": type_, "content": content}

    response = client.analyze_sentiment(request={"document": document})
    sentiment = response.document_sentiment

    #sentiment score is (-1.0, 1.0) and magnitude is (0.0, +inf) and how important it is overall.
    print("Score: {}".format(sentiment.score))
    print("Magnitude: {}".format(sentiment.magnitude))

def main():
    content = ' '.join(sys.argv[1:])
    sentiment_analysis(content)

if __name__ == "__main__":
    main()
