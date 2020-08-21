from django.shortcuts import render
from rest_framework.views import APIview
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from serializers import *
from models import *

# Create your views here.
class Users(APIview):
	"""
	List all users, or create new user.
	"""
	def get(self, request, pk, format=None):
		users = Users.object.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersDetails(APIview):
	"""
	Retrieve, update or delete a user instance.
	"""
	def get_object(self, pk):
		try:
			return Users.objects.get(pk=pk)
		except Users.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		user = Users.object.get(pk=pk)
		serializer = UserSerializer(user)
		return Response(serializer.data)
	
	def put(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class Dogs(APIview):
	"""
	List all users, or create new user.
	"""
	def get(self, request, pk, format=None):
		users = Dogs.object.all()
		serializer = DogSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = DogSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DogsDetails(APIview):
	"""
	Retrieve, update or delete a dog instance.
	"""
	def get_object(self, pk):
		try:
			return Dogs.objects.get(pk=pk)
		except Dogs.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		user = Dogs.object.get(pk=pk)
		serializer = DogSerializer(user)
		return Response(serializer.data)
	
	def put(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = DogSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class DogSize(APIview):
	"""
	List all dog sizes
	"""
	def get(self, request, pk, format=None):
		users = DogSize.object.all()
		serializer = DogSizeSerializer(users, many=True)
		return Response(serializer.data)

class DogSizeDetails(APIview):
	"""
	List a dog size instance.
	"""
	def get_object(self, pk):
		try:
			return DogSize.objects.get(pk=pk)
		except DogSize.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		user = DogSize.object.get(pk=pk)
		serializer = DogSizeSerializer(user)
		return Response(serializer.data)

class Schedules(APIview):
	"""
	List all schedules, create new schedules.
	"""
	def get(self, request, pk, format=None):
		users = Schedules.object.all()
		serializer = ScheduleSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ScheduleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SchedulesDetails(APIview):
	"""
	Retrieve, update or delete a schedule instance.
	"""
	def get_object(self, pk):
		try:
			return Schedules.objects.get(pk=pk)
		except Schedules.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		user = Schedules.object.get(pk=pk)
		serializer = ScheduleSerializer(user)
		return Response(serializer.data)
	
	def put(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = ScheduleSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class ScheduledWalks(APIview):
	"""
	List all scheduled walks, create a new scheduled walk.
	"""
	def get(self, request, pk, format=None):
		users = ScheduledWalks.object.all()
		serializer = ScheduledWalkSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ScheduledWalkSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
class ScheduledWalksDetails(APIview):
	"""
	Retrieve, update or delete a scheduled walk instance.
	"""
	def get_object(self, pk):
		try:
			return ScheduledWalks.objects.get(pk=pk)
		except ScheduledWalks.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		user = ScheduledWalks.object.get(pk=pk)
		serializer = ScheduledWalkSerializer(user)
		return Response(serializer.data)
	
	def put(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = ScheduledWalkSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class Walkers(APIview):
	"""
	List all walkers, create a new walker.
	"""
	def get(self, request, pk, format=None):
		users = Walkers.object.all()
		serializer = WalkerSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = WalkerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WalkersDetails(APIview):
	"""
	Retrieve, update or delete a walker instance.
	"""
	def get_object(self, pk):
		try:
			return Walkers.objects.get(pk=pk)
		except Walkers.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		user = Walkers.object.get(pk=pk)
		serializer = WalkerSerializer(user)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = WalkerSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)