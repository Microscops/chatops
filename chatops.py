from errbot import BotPlugin, botcmd, arg_botcmd, webhook
import random
import string
import itertools


class Chatops(BotPlugin):
    """
    chatops
    """

    def activate(self):
        """
        Triggers on plugin activation

        You should delete it if you're not using it to override any default behaviour
        """
        super(Chatops, self).activate()

    def deactivate(self):
        """
        Triggers on plugin deactivation

        You should delete it if you're not using it to override any default behaviour
        """
        super(Chatops, self).deactivate()

    def get_configuration_template(self):
        """
        Defines the configuration structure this plugin supports

        You should delete it if your plugin doesn't use any configuration like this
        """
        return {'EXAMPLE_KEY_1': "Example value",
                'EXAMPLE_KEY_2': ["Example", "Value"]
               }

    def check_configuration(self, configuration):
        """
        Triggers when the configuration is checked, shortly before activation

        Raise a errbot.ValidationException in case of an error

        You should delete it if you're not using it to override any default behaviour
        """
        super(Chatops, self).check_configuration(configuration)

    def callback_connect(self):
        """
        Triggers when bot is connected

        You should delete it if you're not using it to override any default behaviour
        """
        pass

    def callback_message(self, message):
        """
        Triggered for every received message that isn't coming from the bot itself

        You should delete it if you're not using it to override any default behaviour
        """
        pass

    def callback_botmessage(self, message):
        """
        Triggered for every message that comes from the bot itself

        You should delete it if you're not using it to override any default behaviour
        """
        pass

    @webhook
    def example_webhook(self, incoming_request):
        """A webhook which simply returns 'Example'"""
        return "Example"

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def example(self, message, args):
        """A command which simply returns 'Example'"""
        return "Example"

    @arg_botcmd('name', type=str)
    @arg_botcmd('--favorite-number', type=int, unpack_args=False)
    def hello(self, message, args):
        """
        A command which says hello to someone.

        If you include --favorite-number, it will also tell you their
        favorite number.
        """
        if args.favorite_number is None:
            return f'Hello {args.name}.'
        else:
            return f'Hello {args.name}, I hear your favorite number is {args.favorite_number}.'

    @botcmd(split_args_with=None)
    def randomlaugh(self, mess, args):
        return ''.join(random.choice(string.ascii_letters) for x in range(10))

    @botcmd(split_args_with=None)
    def sum(self, mess, args):
        args = [int(arg) for arg in args]
        return sum(args)

    @arg_botcmd('third_arg', type=str)
    @arg_botcmd('second_arg', type=str)
    @arg_botcmd('first_arg', type=str)
    def argp(self, mess, first_arg=None, second_arg=None, third_arg=None):
        return f"First argument is {first_arg}\n Second argument is {second_arg}\n Third argument is {third_arg}."

    @arg_botcmd('second_arg', type=str)
    @arg_botcmd('first_arg', type=str)
    def deploy(self, mess, first_arg=None, second_arg=None):
        return f"Deploying {first_arg} to {second_arg}."

    @arg_botcmd('first_arg', type=str)
    def create_release(self, mess, first_arg=None):
        return f"Creating release for {first_arg}."

    @arg_botcmd('first_arg', type=str)
    def create_repository(self, mess, first_arg=None):
        return f"Creating repository {first_arg}."

    @arg_botcmd('first_arg', type=str)
    def create_repository(self, mess, first_arg=None):
        return f"Creating repository for {first_arg}."

    @botcmd(split_args_with=None)
    def list_users(self, mess, args):
        return f"There is no users module for now."

    @botcmd(split_args_with=None)
    def list_admins(self, mess, args):
        return f"No admins around."


