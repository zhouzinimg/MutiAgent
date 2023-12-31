'''
reflect_memory
'''
from loguru import logger

from config.config import ConfigForChatgptKwangs
from utils.llm_openai import openai_llm
from utils.prompt_helper import base_kwargs

if __name__ =='__main__':
    memories='''
        唐三走进了一间酒馆，他的眼前一片热闹和喧嚣。酒馆里人声鼎沸，酒杯碰撞的声音不绝于耳。唐三找了一个角落坐下，环顾四周，发现这里的客人五花八门，有武林高手、江湖豪客，还有一些普通的喝酒聊天的人。
        
        正当唐三准备叫服务员的时候，一位看起来威风凛凛的中年人走了过来。他身穿一身黑色长袍，手里还拿着一把巨大的宝剑。他坐在唐三对面的桌子上，露出了一个狡黠的笑容。
        
        "嘿，年轻人，看起来你是个有趣的家伙。要不要来玩一个游戏？"中年人说道。
        
        唐三有些好奇，他问道："什么游戏？"
        
        中年人笑着解释道："我叫做剑魔，是这里的常客。我在这个酒馆里设下了一个小小的挑战，想看看有没有人能够接受。只要你能够在我挥剑的同时，用酒杯接住剑身上的酒滴，我就愿意请你喝一杯。但是如果你接不住，那就得请我喝一杯。怎么样，敢挑战吗？"
        
        唐三听了剑魔的话，眉头微微一皱，这个挑战听起来确实有些困难，但他一向好胜，决定接受挑战。
        
        两人站在酒馆的中央，剑魔举起手中的宝剑，酒滴从剑身上滴落下来。唐三凝神观察，等待着最佳时机。
        
        剑魔挥剑而下，酒滴从剑身上飞溅而出。唐三眼神锐利，他快速反应，用酒杯接住了其中一滴酒滴。酒杯中的酒滴晶莹剔透，美丽而诱人。
        
        观众们欢呼起来，大家都被唐三的技巧所惊叹。剑魔也露出了一丝赞许的笑容，他没有想到自己的挑战会被如此轻松地接受。
        
        "年轻人，你的技巧着实让我刮目相看。来，这杯酒就当是我给你的奖励。"剑魔说着，满满地倒了一杯美酒递给了唐三。
        
        唐三接过酒杯，和剑魔一同举杯庆祝。整个酒馆都为他们的精彩表演而沸腾，唐三也因此结识了许多新朋友。
        
        从那天开始，唐三成为了酒馆里的传奇人物，他的名字在江湖中广为流传。每当有人听说唐三的故事时，都会被他那独特的勇气和技巧所折服。
        
        唐三也渐渐明白，这个世界上不仅有武力的角逐，还有各种各样的有趣挑战和机遇。他决定继续在这个酒馆里度过一段时光，接受更多的挑战，结交更多的朋友。唐三的故事因为这个酒馆而更加精彩纷呈，而酒馆也因着唐三的存在而变得更加热闹和有趣。
        
        而剑魔，他在唐三的帮助下，也逐渐放下了自己的孤独和傲气，成为了唐三最亲密的朋友之一。他们共同在酒馆里举办了许多有趣的活动，吸引了更多的人前来参与和观看。
        
        这间酒馆成为了一个聚集了各种才艺和挑战的场所，人们在这里不仅可以品味美酒，还可以欣赏到各种精彩的表演和竞技。唐三的故事也在这个酒馆里不断延续，每一个到来的人都期待着能够与他一同创造出新的传奇。
        
        从此，这间酒馆成为了一个传说中的地方，人们在谈论它时总是带着敬畏和向往的神情。而唐三，作为这个传说中的主角，他的名字也被载入了历史的篇章中。
    '''
    prompt=f'''
    根据下方的内容提炼出你认为可能有用的结论。并以list[str]形式输出。
    ###
    {memories}
    ###
    OutPut:
    ["结论1",
    "
    '''
    logger.info(openai_llm(kwargs=base_kwargs(prompt))['choices'][0]['message']['content'])
