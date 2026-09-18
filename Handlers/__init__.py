from aiogram import Router
from Handlers.start_bot import router_start
from Handlers.Create_post_bot import router_create_post
from Handlers.Redact_post_bot import redact_post_router
from Handlers.Send_content_bot import send_post_router

Handlers_router = Router()
Handlers_router.include_routers(
    router_start,
    router_create_post,
    redact_post_router,
    send_post_router
)
