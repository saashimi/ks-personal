""" Create a new class, SMS_store. The class will instantiate SMS_store objects,
similar to an inbox or outbox on a cellphone:

my_inbox = SMS_store()

This store can hold multiple SMS messages (i.e. its internal state will just be
 a list of messages). Each message will be represented as a tuple:

(has_been_viewed, from_number, time_arrived, text_of_SMS)

The inbox object should provide these methods:
my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS) # Makes new 
SMS tuple, inserts it after other messages # in the store. When creating this
message, its # has_been_viewed status is set False. 

my_inbox.message_count() # 
Returns the number of sms messages in my_inbox

my_inbox.get_unread_indexes() # 
Returns list of indexes of all not-yet-viewed SMS messages 

my_inbox.get_message(i)
# Return (from_number, time_arrived, text_of_sms) for message[i] # Also change 
its state to "has been viewed". # 

If there is no message at position i, return 
None 

my_inbox.delete(i) # Delete the message at index i

my_inbox.clear() # 
Delete all messages from inbox

Write the class, create a message store object, write tests for these methods, 
and implement the methods."""


class SMS_store(object):

	def __init__(self):
		self.inbox = [] # this is where you add all your attributes

	def add_new_arrival(self, from_number, time_arrived, text_of_SMS, 
						has_been_viewed = False):
		msg = (has_been_viewed, from_number, time_arrived, text_of_SMS)
		self.inbox.append(msg)
		
	def message_count(self):
		return len(self.inbox)
		
	def get_unread_indexes(self):
		unread = []
		for index in range(len(self.inbox)):
			if self.inbox[index][0] == False:
				unread.append(index)
		return unread
	
	def get_messages(self, i):
		has_been_viewed, from_number, time_arrived, text_of_SMS = self.inbox[i]
		has_been_viewed = True


	def delete(self, i):
		del self.inbox[i]
		
	def clear(self):
		self.inbox = []
		
if __name__ == "__main__":
	myPhone = SMS_store()
	myPhone.add_new_arrival("555-5555", "03:05 PM", "I can haz?", False)
	myPhone.add_new_arrival("555-5555", "03:06 PM", "cheezburger?", False)
	myPhone.add_new_arrival("555-5555", "03:07 PM", "Yah?", True)
	print(myPhone.inbox)
	print(myPhone.get_messages(1))

	"""	
	myPhone = SMS_store()
	myPhone.add_new_arrival("555-5555", "03:05 PM", "I can haz?", False)
	myPhone.add_new_arrival("555-5555", "03:06 PM", "cheezburger?", False)
	myPhone.add_new_arrival("555-5555", "03:07 PM", "Yah?", True)
	print(myPhone.message_count())
	print(myPhone.get_unread_indexes())
	myPhone.delete(1)
	print(myPhone.inbox)
	myPhone.clear()
	print(myPhone.inbox)
	"""