import imp
from multiprocessing import context
import re
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from . import models
# Create your views here.

def Home(request):
    # return HttpResponse("hi welcome to django")
    
    context = {
        "my_obj":[
            {
                "title":"شلیک به دشمنان اهریمنی – One Shell Straight to Hell PC Game",
                "body":"توضیحات بازی: بازی One Shell Straight to Hell بار دیگر شخصیت پادر را با یک بازگشت هیجان انگیز روبرو می‌کند. گیم‌پلی این بازی همان حال و هوای قدیمی خودش را دارد و قرار است که یک تجربه راگ لایت هیجان انگیز را داشته باشید. بازی روی المان‌های دفاعی استوار شده است و بازهم جهان با نظمی را می‌بینیم که در طول تجربه‌ی خود، حقایق بیشتری از آن را کشف خواهید کرد. در این بازی رفتارهای انسانی و اهریمی در هم آمیخته است و به‌صورت کنایه آمیزی می‌توانید آن‌ها را تجربه کنید. شما یک فرد معمولی هستید که در جمع، قصد دارید به‌صورت کاملا منطقی عمل کرده و زندگی خود را نجات دهید. One Shell Straight to Hell در سبک اکشن و ماجرایی می باشد که توسط استودیو Shotgun with Glitters طراحی شده است و کمپانی Feardemic آن را برای کامپیوتر منتشر کرده است، این بازی دارای گیم پلی و داستان فوق العاده جذابی می باشد. پیشنهاد میکنیم این بازی زیبا را از دست ندهید…",
                "image":"http://pocketgames.ir/wp-content/uploads/2021/02/One-Shell-Straight-to-Hellp.jpg",        
            },  
            {
                "title":"برای پادشاه – For The King Lost Civilization PC Game",
                "body":"توضیحات بازی: بازی For The King از آن دسته بازی های خوش ساخت و موفق است که توانسته فروش بسیار خوبی داشته باشد و هم چنین، نظر مثبت بسیاری از کاربران را به خود جلب کند. نقشه‌ها، ماموریت‌ها و حوادث بازی به صورت تصادفی ایجاد می‌شوند که تجربه جدید و منحصربه‌فردی را برای هر یک از بازیکنان به ارمغان می‌آورد. همچنین این بازی دارای بخش تک‌نفره و کوآپ (آفلاین و آنلاین) است و به این خاطر بازیکنان می‌توانند به تنهایی یا با دوستان خود به تجربه بازی اقدام کنند. کمپین کیک‌استارتر دانلود بازی For The King در سال ۲۰۱۵ راه‌اندازی شد و در حالی که هدف سازندگان تنها جمع‌آوری ۳۰ هزار دلار بود، به مبلغ ۸۷ هزار و ۵۰۰ دلار دست یافت. For The King Lost Civilization در سبک ماجرایی و استراتژیک می باشد که توسط استودیو IronOak Games طراحی شده است و کمپانی Curve Digital آن را برای کامپیوتر منتشر کرده است، این بازی دارای گیم پلی و داستان فوق العاده جذابی می باشد. پیشنهاد میکنیم این بازی زیبا را از دست ندهید…",
                "image":"http://pocketgames.ir/wp-content/uploads/2021/02/For-The-King-Lost-Civilizationp.jpg",        
            },
            {
                "title":"کلان شهر – Mutropolis PC Game",
                "body":"توضیحات بازی: در بازی Mutropolis شما قرار است که به یک کاراگاه دوست داشتنی تبدیل شده و گیم‌پلی بازی را در سبک اشاره و کلیک دنبال کنید. بازی در سال ۵۰۰۰ جریان دارد و قرار است که نظاره‌گر بزرگ‌ترین دستاوردهای تاریخ بشریت باشیم. اهرام، مونالیزا، شاهزاده‌های فراموش شده و خیلی از المان‌های دیگر را در بازی شاهد هستیم. همه‌ی آن‌ها فراموش شده‌اند و تنها هنری دیژون و تیم باستان شناس وی هستند که باقی مانده‌اند. آن‌ها مریخ را ترک کرده‌اند تا بتوانند گنجینه‌های از دست رفته را در سیاره وحشی زمین پیدا کنند. آن‌ها زندگی شیرین خود را به امید پیدا کردن چنین چیزهایی رها کرده و حال چیزهای عجیب و غریبی را در زمین تجربه خواهند کرد. شما همراه با هنری قرار است که در ویرانه‌های تمردن قدم زده و با دیگر شخصیت‌ها همراه شوید. همیشه سولاتی از شما پرسیده خواهد شد که این شخصیت‌ها که بوده‌اند و چه کارهایی انجام داده‌اند. Mutropolis در سبک ماجرایی می باشد که توسط استودیو Pirita Studio طراحی شده است و کمپانی Application Systems Heidelberg آن را برای کامپیوتر منتشر کرده است، این بازی دارای گیم پلی و داستان فوق العاده جذابی می باشد. پیشنهاد میکنیم این بازی زیبا را از دست ندهید…",
                "image":"http://pocketgames.ir/wp-content/uploads/2021/02/Mutropolisp.jpg",        
            },
        ],   
        "username":"amirhosein",
        "age":21,
        "job":"programmer",
        'articles': models.Article.objects.all().order_by('-publish').filter(status="p"),
        'new_post': models.Article.objects.all().order_by("-publish")[0]
        
    }
    return render(request , 'blog/home.html' , context)



def detail_article(request , article_slug):
    context = {
        "article" : models.Article.objects.get(slug = article_slug)
    }

    return render(request, 'blog/detail.html' , context)

def posts(request):
    context = {
        'article' : models.Article.objects.all().order_by('-publish')
    }
    return render(request , "blog/posts.html" , context)

def api(request):
    return JsonResponse({'title':"سلام دنیا"})
