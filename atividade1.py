{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mdesouzasilva571-pixel/23-08-2025/blob/main/atividade1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def contar_vogais_consoantes(frase):\n",
        "    vogais = \"aeiou\"\n",
        "    consoantes = \"bcdfghjklmnpqrstvwxyz\"\n",
        "\n",
        "    total_vogais = 0\n",
        "    total_consoantes = 0\n",
        "\n",
        "    for letra in frase.lower():  # .lower() para não diferenciar maiúsculas de minúsculas\n",
        "        if letra in vogais:\n",
        "            total_vogais += 1\n",
        "        elif letra in consoantes:\n",
        "            total_consoantes += 1\n",
        "\n",
        "    return total_vogais, total_consoantes\n",
        "\n",
        "\n",
        "# Programa principal\n",
        "frase_input = input(\"Digite uma frase: \")\n",
        "vogais, consoantes = contar_vogais_consoantes(frase_input)\n",
        "\n",
        "print(f\"Número de vogais: {vogais}\")\n",
        "print(f\"Número de consoantes: {consoantes}\")"
      ],
      "metadata": {
        "id": "IXIoKp-zI95b"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "name": "Damos-lhe as boas-vindas ao Colab",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}