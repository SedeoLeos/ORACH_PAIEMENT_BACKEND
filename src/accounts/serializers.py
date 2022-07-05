# posts/serializers.py
from rest_framework import serializers
from .models import CustomUser,cotisation,versement



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__' 
    
    def save(self):
        user =CustomUser(
            email=self.validated_data['email']
        )
        password =self.validated_data['password']
        
        user.set_password(password)
        
        print(user.password)
        user.save()
        return user
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return CustomUser.objects.filter(username=username)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id',  'username', 'password','first_name','last_name','sexe','dateNaiss','profession',"fonction",'telephone')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name','last_name','sexe','dateNaiss','profession',"fonction",'telephone', 'email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user( validated_data['email'], validated_data['password'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],sexe=validated_data['sexe'],dateNaiss=validated_data['dateNaiss'],profession=validated_data['profession'],telephone=validated_data['telephone'])

        return user
    

class CotisationSerializers(serializers.ModelSerializer):
    class  Meta:
        model = cotisation
        fields = "__all__"
        
class VersementSerializers(serializers.ModelSerializer):
    class  Meta:
        model = versement
        fields = "__all__"
