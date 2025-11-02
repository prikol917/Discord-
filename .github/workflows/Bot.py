 append(line)

        for entry in slots_raw:
            try:
                num, name = entry.split(" ", 1)
                num = int(num)
                current_slots[num] = {"name": name, "user": None}
            except:
                pass

        embed = discord.Embed(
            title="Запись на поход",
            description="\n".join(header),
            color=0x00ff99
        )

        last_embed_message = await ctx.send(embed=embed, view=SignupView())

        try:
            await ctx.message.delete()
        except discord.Forbidden:
            await ctx.send("⚠️ У меня нет прав удалять сообщения. Добавь 'Manage Messages'.")

# ==============================
# Авто-перезапуск бота
# ==============================
async def run_bot():
    while True:
        try:
            bot = commands.Bot(command_prefix="!", intents=intents)
            setup_commands(bot)
            print("🔹 Подключаемся к Discord...")
            await bot.start(TOKEN)
        except Exception:
            print("❌ Ошибка в боте, перезапуск через 5 секунд")
            traceback.print_exc()
            await asyncio.sleep(5)

# ==============================
# Запуск
# ==============================
if name == "__main__":
    asyncio.run(run_bot())
