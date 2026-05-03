from django.shortcuts import render
from django.http import Http404
  
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class RetrieveData(APIView):
     def get(self, request):
        conn = None
        try:
            import pymysql
            conn = pymysql.connect(host='devdbrds.cfgu9s5ykxy0.ap-southeast-1.rds.amazonaws.com', user='admin', passwd='Admin$2020$12!%', db='devai')
            cur = conn.cursor()
            cur.execute("SELECT resume_id,resume_text FROM devai.nr_resume_text LIMIT 100")
            fetched_data = cur.fetchall()
            res_list = [x for x in fetched_data]
            # json_res_data = {"id": res_list[0],"Resume_Text": res_list[1]}
            json_res_data = {"Resume_Text": res_list}
            return Response({"data": json_res_data})
            # cur.close()
            # conn.close()
        except Exception as e:
            return Response({"error": 'Error'})
        finally:
            if conn is not None:
                conn.close()





                            

      






















#









# from django.db.models import Q
# results = BlogPost.objects.filter(Q(title__icontains=your_search_query) | Q(intro__icontains=your_search_query) | Q(content__icontains=your_search_query))