# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Rutgers University Voice Assistant activated. How may I help you today?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class EventsInfoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("EventsInfoIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Today from 7:30 pm to 10:30 pm, there is a Scarlet Fest Black Light Nerf Archery event."

        return (
            handler_input.response_builder.speak(speak_output).ask(speak_output).response
        )

class FoodInfoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FoodInfoIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "According to Rutgers Dining Services, today at the Gourmet kitchen you have Grilled Marinated Tilapia, Cheese and Bean Enchiladas, Cilantro Lime Brown Rice, Roasted Carrots, Smashed Black Beans, Shredded Iceberg Lettuce, 6-inch Flour Tortilla, Pico de Gallo, Shredded Cheddar Cheese, and Sour Cream."

        return (
            handler_input.response_builder.speak(speak_output).ask(speak_output).response
        )    

class UniversityInfoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("UniversityInfoIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "The final exam period for spring 2023 is from Thursday may 4th to Wednesday May 10th."

        return (
            handler_input.response_builder.speak(speak_output).ask(speak_output).response
        )

class StudentInfoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("StudentInfoIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "According to your profile, you have quiz 4 from distributed and cloud computing due on apr 20th, module 12 assignment from business analytics due on apr 16th."

        return (
            handler_input.response_builder.speak(speak_output).ask(speak_output).response
        )

class TeacherInfoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("TeacherInfoIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "This course is being taught by Professor Ian Lebbern."

        return (
            handler_input.response_builder.speak(speak_output).ask(speak_output).response
        )

class ShuttleInfoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("ShuttleInfoIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Monday through Thursday, the shuttle operates from 7:00 AM until 10:00 PM. Shuttles will now depart every 5 minutes from City Lot 15 from 7:00 AM until 10:00 AM; depart every 10 minutes from 10 AM until 7:20 PM; and every 20 minutes from 7:20 PM until its last departure from City Lot 15 at 9:40 PM. On Fridays, the shuttle operates from 7:00 AM until 7:00 PM; departing from City Lot 15 every 20 minutes"

        return (
            handler_input.response_builder.speak(speak_output).ask(speak_output).response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "How can I help you today?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure about that. Is there anything else you would like to know?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(EventsInfoIntentHandler())
sb.add_request_handler(FoodInfoIntentHandler())
sb.add_request_handler(UniversityInfoIntentHandler())
sb.add_request_handler(StudentInfoIntentHandler())
sb.add_request_handler(TeacherInfoIntentHandler())
sb.add_request_handler(ShuttleInfoIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()