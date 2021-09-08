from transformers import T5Tokenizer, AutoModelForCausalLM, TFAutoModelForCausalLM, AutoTokenizer


def create_single_text_message(message):
    """
    if message == 'ありがとう':
        message = 'どういたしまして！'
    if message == '今日の天気は':
        message = '雨に決まってるだろうが'
    if message == 'こんにちは':
        message = 'こんちはー'
    """
    #sentence=message
    print(message)
    #"""
    #入力文字
    enter = '<s>{}[SEP]'.format(message)

    # トークナイザーとモデルの準備
    tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")
    #print(tokenizer.all_special_ids)

    #モデル
    #model = AutoModelForCausalLM.from_pretrained("../../chat_new_5")
    #model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-medium")
    model = AutoModelForCausalLM.from_pretrained("kaedefuto/chat_bot")
    # 推論
    pt_tensor = tokenizer.encode(enter, return_tensors="pt")

    output = model.generate(
        input_ids=pt_tensor,
        do_sample=True,
        top_p=1.0,
        top_k=50,
        early_stopping=True,
        max_length=50,
        min_length=10,
        num_return_sequences=1,
        output_scores=True,
        bad_words_ids=[[1], [5]]
    )
    outer = tokenizer.batch_decode(output)

    #</s>の削除
    outer = [s.replace('</s>','') for s in outer]
    outer = [s.replace('<unk>','') for s in outer]
    for i in outer:
        sentence=i.replace("<s>","").replace("[SEP]","").replace(message,"")

    print(sentence)
    #"""
    test_message = [
                {
                    'type': 'text',
                    'text': sentence
                }
            ]
    return test_message
