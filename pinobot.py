#!/bin/env python
import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
global index
comuni = {"Acerra", "Afragola", "Agerola", "Anacapri", "Arzano", "Bacoli", "Barano d'Ischia", "Boscoreale", "Boscotrecase", "Brusciano", "Caivano", "Calvizzano", "Camposano", "Capri", "Carbonara di Nola", "Cardito", "Casalnuovo di Napoli", "Casamarciano", "Casamicciola Terme", "Casandrino", "Casavatore", "Casola di Napoli", "Casoria", "Castellammare di Stabia", "Castello di Cisterna", "Cercola", "Cicciano", "Cimitile", "Comiziano", "Crispano", "Ercolano", "Forio", "Frattamaggiore", "Frattaminore", "Giugliano in Campania", "Gragnano", "Grumo Nevano", "Ischia", "Lacco Ameno", "Lettere", "Liveri", "Marano di Napoli", "Mariglianella", "Marigliano", "Massa Lubrense", "Massa di Somma", "Melito di Napoli", "Meta", "Monte di Procida", "Mugnano di Napoli", "Napoli", "Nola", "Ottaviano", "Palma Campania", "Piano di Sorrento", "Pimonte", "Poggiomarino", "Pollena Trocchia", "Pomigliano d'Arco", "Pompei", "Portici", "Pozzuoli", "Procida", "Qualiano", "Quarto", "Roccarainola", "San Gennaro Vesuviano", "San Giorgio a Cremano", "San Giuseppe Vesuviano", "San Paolo Bel Sito", "San Sebastiano al Vesuvio", "San Vitaliano", "Sant'Agnello", "Sant'Anastasia", "Sant'Antimo", "Sant'Antonio Abate", "Santa Maria la Carità", "Saviano", "Scisciano", "Serrara Fontana", "Somma Vesuviana", "Sorrento", "Striano", "Terzigno", "Torre Annunziata", "Torre del Greco", "Trecase", "Tufino", "Vico Equense", "Villaricca", "Visciano", "Volla"}

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()
TOKEN = os.getenv('TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ciao Pino! Sei di Agnano?")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global index
    text = update.message.text.strip().lower()  # Rimuove spazi e converte in minuscolo

    if text in ('si', 'ok', 'sì'):
        response = "Grande Pino! siamo venuti al mondo per puro diletto di un Dio sadico che ama vederci soffrire di malesseri psicologici inesistenti."
    else:
        comuni_list = list(comuni)  # Converti il set in lista per accesso con indice
        if index >= len(comuni_list):  # Evita errori di indice fuori limite
            index = 0  
        response = "Ciao Pino! sei di " + comuni_list[index] + "?"
        index += 1

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


if __name__ == '__main__':
    index = 0
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    chat_handler = MessageHandler(None, chat)    
    application.add_handler(chat_handler)

    application.run_polling()
