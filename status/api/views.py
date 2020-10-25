from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from status.models import Status 
from .serializers import StatusSerializer

# class StatusListAPIView(APIView):
# 	permission_classes = []
# 	authentication_classes = []

# 	def get(self, request, *args,**kwargs):
# 		qs = Status.objects.all()
# 		serializer = StatusSerializer(qs, many=True)
# 		return Response(serializer.data)

# 	def post(self,request,*args,**kwargs):
# 		qs = Status.objects.all()
# 		serializer = StatusSerializer(qs,many=True)
# 		return Response(serializer.data)


class StatusListAPIView(generics.ListAPIView):
	# queryset = Status.objects.all()	
	serializer_class = StatusSerializer
	permission_classes = []
	authentication_classes = []

	#search
	def get_queryset(self):
		qs = Status.objects.all()	
		q = self.request.GET.get('q')
		if q is not None:
			qs = qs.filter(content__icontains=q)
		return qs


class StatusCreateAPIView(generics.CreateAPIView):
	queryset = Status.objects.all()		
	serializer_class = StatusSerializer
	permission_classes = []
	authentication_classes = []

	# def perform_create(self,serializer):
	# 	serializer.save(user=self.request.user)

class StatusDetailAPIView(generics.RetrieveAPIView):
	queryset = Status.objects.all()
	lookup_field = 'id'	
	serializer_class = StatusSerializer
	permission_classes = []
	authentication_classes = []

	# def get_object(self,*args,**kwargs):

	# 	kwarg = self.kwargs
	# 	kwarg_id = kwarg.get('pid')
	# 	return Status.objects.get(id=kwarg_id)

class StatusUpdateAPIView(generics.UpdateAPIView):
	queryset = Status.objects.all()
	# lookup_field = 'id'	
	serializer_class = StatusSerializer
	permission_classes = []
	authentication_classes = []

	# def get_object(self,*args,**kwargs):
	# 	kwarg = self.kwargs
	# 	kwarg_id = kwarg.get('pk')
	# 	return Status.objects.get(id=kwarg_id)


class StatusDeleteAPIView(generics.DestroyAPIView):
	queryset = Status.objects.all()
	# lookup_field = 'id'	
	serializer_class = StatusSerializer
	permission_classes = []
	authentication_classes = []


#IN-BUILT APIVIEWS(generics)(CRUD)
# generics - ListCreateAPIView
# generics - RetrieveUpdateAPIView
# generics - RetrieveDestroyAPIView
# generics - RetrieveUpdateDestroyAPIView


#mixins-

class StatusMixinCreateAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	serializer_class = StatusSerializer
	permission_classes = []
	authentication_classes = []

	#createmodelmixin method
	def post(self,request,*args,**kwargs):
		return self.create(request,*args,*kwargs)


class StatusMixinUpdateAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
	serializer_class = StatusSerializer
	permission_classes = []
	authentication_classes = []

	#Updatelmixin method
	def put(self,request,*args,**kwargs):
		return self.update(request,*args,*kwargs)

	#Deletemixin method
	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,*kwargs)

class StatusRetrieveUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Status.objects.all()
	serializer_class = StatusSerializer
	permission_classes = []
	authentication_classes = []

#ONE CRUD OPERATION- USINGS MIXINS

class StatusMixinsAPIView(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.ListAPIView):
	serializer_class = StatusSerializer
	permission_classes = [permissions.IsAuthenticated]
	authentication_classes = [SessionAuthentication]

	def get_queryset(self,*args,**kwargs):
		qs = Status.objects.all()
		request = self.request
		query = request.GET.get('q')

		if query is not None:
			qs = qs.filter(content__icontains=query)
		return qs

	def get_object(self):
		request = self.request
		queryset = self.get_queryset()
		passed_id = request.GET.get('id',None)
		obj = None
		if passed_id is not None:
			obj = queryset.filter(id=passed_id)
			self.check_object_permissions(request,obj)

		return obj

	def post(self, request, *args,**kwargs):
		return self.create(request,*args,**kwargs)

	#Updatelmixin method
	def put(self,request,*args,**kwargs):
		return self.update(request,*args,*kwargs)

	def patch(self,request,*args,**kwargs):
		return self.update(request,*args,*kwargs)

	#Deletemixin method
	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,*kwargs)



