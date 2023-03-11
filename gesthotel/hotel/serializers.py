from rest_framework import serializers
from .models import Hotel, Room, Client, Reservation

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)
    client = ClientSerializer(read_only=True)
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'        