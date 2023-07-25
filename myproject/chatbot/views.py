import openai
from django.shortcuts import render



def chatbot_view(request):
    chatbot_output = ''
    if request.method == 'POST':
        # lấy dữ liệu đầu vào
        user_input = request.POST.get('user_input')
        # api key của openai
        openai.api_key = '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' 
        # lấy câu trả lời từ mô hình đã được huấn luyện text-davinci-002 với dữ liệu đầu vào là user-input
        response = openai.Completion.create(
            engine="text-davinci-003",  
            prompt=user_input,
            max_tokens=100 # ~75 words
        )
        # chỉ lấy phần từ đầu tiên của dict
        chatbot_output = response['choices'][0]['text'] 
    # trả về trang web chatbot.html để hiển thị output
    return render(request, 'chatbot.html', {'chatbot_output': chatbot_output})
