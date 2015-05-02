TheZineREST
===========

![TheZineRest](https://s3.amazonaws.com/mixture-mixed/2967/5505/assets/img/logo-white.png)

Unofficial REST API for blog [The 'Zine](http://thezine.biz/)

Start
=====

    $ python zine.py                     # start the script at server
    
Usage
===== 

**Base URL:** [http://thezine.herokuapp.com/](http://thezine.herokuapp.com/)

**Output:** JSON

`GET /v1/articles/<count>`

``` http://thezine.herokuapp.com/v1/articles/1
    
        {"meta": {"is_successful": true, "code": 200}, "data": {"no_of_articles": 9, "articles": [{"tagline": "A New Beginning...", "title": "The Editorial", "author": {"contacts": {"email": "meghna.adore.97@gmail.com", "twitter": "https://twitter.com/DespicableMe53", "facebook": "https://www.facebook.com/meghna2803", "link": ""}, "name": "Meghna Gulati", "image_url": "https://s3.amazonaws.com/mixture-mixed/2967/5505/assets/img/authors/meghna.png", "id": "meghna-gulati"}, "id": "issue-1-editorial"}, {"tagline": "On relationships.", "title": "Of Smiles and Tears", "author": {"contacts": {"email": "tanya.dutta498@yahoo.in", "twitter": "", "facebook": "https://www.facebook.com/tanya.dutta49?fref=ts", "link": ""}, "name": "Tanya Dutta", "image_url": "https://s3.amazonaws.com/mixture-mixed/2967/5505/assets/img/authors/tanya.png", "id": "tanya-dutta"}, "id": "issue-1-smiles-tears"}, {"tagline": "We cannot choose where we come from, but we can decide where we go to.", "title": "Plato Speak", "author": {"contacts": {"email": "anirban.touch56@gmail.com", "twitter": "", "facebook": "https://www.facebook.com/Anirban56?fref=ts", "link": ""}, "name": "Anirban Chattopadhyaya", "image_url": "https://s3.amazonaws.com/mixture-mixed/2967/5505/assets/img/authors/anirban.png", "id": "anirban-chattopadhyaya"}, "id": "issue-1-plato"}, {"tagline": "A sports column.", "title": "Slam!", "author": {"contacts": {"email": "zaiddrabu@yahoo.com", "twitter": "", "facebook": "https://www.facebook.com/zaid.drabu?fref=ts", "link": ""}, "name": "Zaid Drabu", "image_url": "https://s3.amazonaws.com/mixture-mixed/2967/5505/assets/img/authors/zaid.png", "id": "zaid-drabu"}, "id": "issue-1-slam"}, {"tagline": "Viewing the world my way.", "title": "Perspective", "author": {"contacts": {"email": "prakritianand22@gmail.com", "twitter": "", "facebook": "https://www.facebook.com/prakriti.anand?fref=ts", "link": ""}, "name": "Prakriti Anand", "image_url": "https://s3.amazonaws.com/mixture-mixed/2967/5505/assets/img/authors/prakriti.png", "id": "prakriti-anand"}, "id": "issue-1-perspective"}, {"tagline": "Overcoming obstacles, beating the blues.", "title": "I. M. Possible", "author": {"contacts": {"email": "meghna.adore.97@gmail.com", "twitter": "https://twitter.com/DespicableMe53", "facebook": "https://www.facebook.com/meghna2803", "link": ""}, "name": "Meghna Gulati", "image_url": "https://s3.amazonaws.com/mixture-mixed/2967/5505/assets/img/authors/meghna.png", "id": "meghna-gulati"}, "id": "issue-1-possible"}, {"tagline": "Review: Swagath, A Restaurant.", "title": "The Good & the Bad", "author": {"contacts": {"email": "chawlarahat@gmail.com", "twitter": "https://twitter.com/ChawlaRahat", "facebook": "https://www.facebook.com/chawlarahat?fref=ts", "link": ""}, "name": "Rahat Chawla", "image_url": "https://s3.amazonaws.com/mixture-mixed/2967/5505/assets/img/authors/rahat.png", "id": "rahat-chawla"}, "id": "issue-1-review"}, {"tagline": "The Journey of a nomadic spirit.", "title": "Travel", "author": {"contacts": {"email": "yashs504@gmail.com", "twitter": "", "facebook": "https://www.facebook.com/yashthegodfather?fref=pb&hc_location=profile_browser", "link": ""}, "name": "Yash Sharma", "image_url": "https://s3.amazonaws.com/mixture-mixed/2967/5505/assets/img/authors/yash.png", "id": "yash-sharma"}, "id": "issue-1-travel"}, {"tagline": "A contribution.", "title": "If I Could Save Time in a Bottle", "author": {"contacts": {"email": "kanikarana13@gmail.com", "twitter": "", "facebook": "https://www.facebook.com/kanika.rana1?fref=ts&ref=br_tf", "link": ""}, "name": "Kanika Rana", "image_url": "https://s3.amazonaws.com/mixture-mixed/2967/5505/assets/img/authors/kanika.png", "id": "kanika-rana"}, "id": "issue-1-death"}]}} 
        
```

`GET /v1/author/<author_id>`

```

        http://thezine.herokuapp.com/v1/author/meghna-gulati
    
        {"meta": {"code": 200, "is_successful": true}, "message": "Author with this id exist", "data": {"name": "Meghna Gulati", "id": "meghna-gulati", "contacts": {"link": "", "facebook": "https://www.facebook.com/meghna2803", "email": "meghna.adore.97@gmail.com", "twitter": "https://twitter.com/DespicableMe53"}, "image_url": "https://s3.amazonaws.com/mixture-mixed/2967/5505/assets/img/authors/meghna.png"}} 
        
```

Contribute
========

Feel free to send a pull request!

Developed By
============

`Abhijeet Mohan` - `void.aby@gmail.com`    

<a href="https://plus.google.com/104070882148677917719/about">
  <img alt="Follow me on Google+"
       src="http://data.pkmmte.com/temp/social_google_plus_logo.png" />
</a>

License
==========================

```
Copyright 2014 Abhijeet Mohan - https://github.com/TheZine/TheZineREST

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
