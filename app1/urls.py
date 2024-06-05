from django.urls import path
from .views import *

from .apis import *

urlpatterns = [
    path('',home,name="home"),
    path('signup',signup,name="signup"),
    path('login',user_login,name="login"),
    path('contactus',contactus,name="contactus"),
    path('contact_us',contact_us,name="contact_us"),
    path('about',about,name="about"),
    path('createuser',createuser,name="createuser"),
    path('logout',logout,name="logout"),
    path('dashboard',dashboard,name="dashboard"),
    path('details/<str:query>',stockdetails,name="stockdetails"),
    path('removewatchlist/<str:symbol>',removewatchlist,name="removewatchlist"),
    path('portfolio',user_portfolio,name="user_portfolio"),
    path('updatestocks',updatestocks,name="updatestocks"),
    path('errorpage',errorpage,name="errorpage"),
    path('settings',settings,name="settings"),
    path('api/search/<str:query>',search,name="search"),
    path('api/watchlist/<str:query>',watchlist,name="watchlist"),
    path('api/fetchdetails/<str:query>',fetchdetails,name="fetchdetails"),
    path('api/graphdata/<str:query>/<str:start>/<str:end>',graphdata,name="graphdata"),
    path('api/portfolio',portfolio,name="portfolio"),
    path('api/portfoliochart',portfoliochart,name="portfoliochart"),
    path('api/incomecalculate',income,name="income"),
    path('api/holdings/<str:query>',holdings,name="holdings"),
]