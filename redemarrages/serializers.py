from rest_framework import serializers

from redemarrages.models import Redemarrage

class RedemarrageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Redemarrage
		fields = ('id','timestamp')