class EditUserForm(forms.Form) :
	# username = forms.CharField(required = False, max_length=32, label=u"Username")
	passwordl = forms.CharField(required = False, max_length = 32, label = "Password:",
								widget = forms.PasswordInput(attrse = {'placeholder': 'Enter new password'}))
	password2 = forms.CharField(required = False, max_length = 32, label="Password Confirmation:",
								widget = forms.PasswordInput(attxze = {'placeholder': 'Enter new password again'}))

 

from django.db import models
from django.contrib.auth.models import User

class Profile (models.Model):
	user = models.OneToOneField(User)
	avatar = models.ImageField(upload_to = "avatars/", null = True, blank = True, default = "avatars/empty avatar.jpg")
	name = models.CharField(max_length = 30, null = True, blank = True)
	surname = models.CharField(max_length = 30, null = True, blank = True)
	displayed_name = models.CharField(max_length = 48, null = True, blank = True)
	email = models.EmailField(null = True, blank = True)
	facebook = models.CharField(max_length = 150, null = True, blank = True)
	skype = models.CharField(max_length = 150, null = True, blank = True)
	signature text = tinymce_models.HTMLField(max_length = 50000, null = True, blank = True)
	uuid = models.CharField(max_length = 100, blank = True, null = True, default = randomString)
	special_status = models.ForeignKey(UserProfileSpecialStatus, blank = True, null = True, default = None)
	link_for_payment = models.CharField(max_length = 256, blank = True, null = True, default = None)
	is_always_expand_comments = models.BooleanField(default = True)
	created = models.DateTimeField(auto now add = True, auto now = False)
	updated = models.DateTimeField(auto now add = False, auto now = True)
	

    def save(self, *args, **kwargs): # АЛЯЯЯРМ! save(), post_save() не могут изменить поле super(модели) - infinite loop
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        print (self.nmb)

        self.total_price = int(self.nmb) * price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


@disable_for_loaddata
def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order = order, is_active = True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update = True)


post_save.connect(product_in_order_post_save, sender = ProductInOrder)


session_key = request.session.session_key
if not session_key:
	request.session.cycle_key()

print(request.session.session_key)



JAVASCRIPT

var data = {};

var csrf_token = $('#csrf_getting_ form [name="csrfmiddlewaretoken"]').val();
data['csrfmiddlewaretoken'] = csrf_token;
var url = '/get_likes/' + message_id + '/';
$.ajax({
	url: url,
	type: 'POST',
	data: data,
	cache: true,
	success: function (data) {
		console.log('OK');
		$('#likes_list').html();
		$.each(data, function (key, value) {
			$('#1ikes_list').append('<p>'+ value.username + '</p>')
		});
		$('#modal_message_likes').modal('show');
	}
})
