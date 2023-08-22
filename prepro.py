{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOHpiJCKBuSrUmSPS3LY1EF",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/okuno-fuka-nalgo-intern/test-okuno/blob/main/prepro.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eX82MwV72hEG",
        "outputId": "167d860c-1803-4703-ab73-c64968729710"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'team-c-2023-summer'...\n",
            "remote: Enumerating objects: 40, done.\u001b[K\n",
            "remote: Counting objects: 100% (40/40), done.\u001b[K\n",
            "remote: Compressing objects: 100% (23/23), done.\u001b[K\n",
            "remote: Total 40 (delta 17), reused 32 (delta 12), pack-reused 0\u001b[K\n",
            "Receiving objects: 100% (40/40), 43.79 KiB | 773.00 KiB/s, done.\n",
            "Resolving deltas: 100% (17/17), done.\n"
          ]
        }
      ],
      "source": [
        "!git clone https://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@github.com/nalgo-intern/team-c-2023-summer.git"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import importlib\n",
        "scraper = importlib.import_module(\"team-c-2023-summer.scraper\")\n",
        "scraper.scraper()"
      ],
      "metadata": {
        "id": "osAzcCtY2ss6"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import re\n",
        "import numpy as np"
      ],
      "metadata": {
        "id": "8coeiPeZ2yWw"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def prepro(data):\n",
        "  f_kakko = lambda x: re.sub(\"\\(.+?\\)\",\"\",str(x))\n",
        "  a = data.applymap(f_kakko)\n",
        "\n",
        "  return a"
      ],
      "metadata": {
        "id": "o8nawaLHGhCc"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_data=pd.read_csv('dataset.csv',header=None, skiprows=1,index_col=0)\n",
        "data = prepro(df_data)\n",
        "print(data)"
      ],
      "metadata": {
        "id": "5S6wyhfn24Jy",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c7cd79cc-fa14-4dec-9d12-00409e9c1bc2"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "               1      2                                                  3\n",
            "0                                                                         \n",
            "0         青い眼の人形   野口雨情  青い眼をした　お人形はアメリカ生まれの　セルロイド日本の港へ　ついたとき一杯涙を　うかべてた...\n",
            "1          仰げば尊し     不詳  あおげばとうとし　わが師の恩教えの庭にも　はやいくとせ思えばいと疾し　この年月今こそわかれめ...\n",
            "2            赤い靴   野口雨情  赤い靴　はいてた　女の子異人さんに　つれられて　行っちゃった横浜の　埠頭から　船に乗って異人...\n",
            "3       赤い帽子白い帽子   武内俊子  赤い帽子白い帽子　仲よしさんいつも通るよ　女の子ランドセルしょって　お手々をふっていつも通る...\n",
            "4           赤とんぼ   三木露風  夕やけ小やけの　赤とんぼ負われて見たのは　いつの日か山の畑の　桑の実を小篭に摘んだは　まぼろ...\n",
            "..           ...    ...                                                ...\n",
            "193      ラジオ体操の歌    藤浦洸  新しい朝が来た　希望の朝だ喜びに胸を開け　大空あおげラジオの声に　健やかな胸をこの香る風に　...\n",
            "194  りんご　みかん　バナナ  長谷川勝士  りんご　りんご　りんごナイフ　ナイフ　ナイフをつかうかわをむく　きれないようにながく　ながく...\n",
            "195         別れの歌     不詳  なごりをおしむ　ことの葉もいまはのべえで　たゞつらしあすはうつゝ　けふはゆめけふはゆめのこる...\n",
            "196     わっ！！おしゃれ   阿部直美  ライオンさんって　わっ　おしゃれ かおをごしごし　わっ　あらう それから　それから　それから...\n",
            "197       われは海の子  文部省唱歌  我は海の子白波のさわぐいそべの松原に煙たなびくとまやこそ我がなつかしき住家なれ生れてしおに浴...\n",
            "\n",
            "[198 rows x 3 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "gNa6npYL25pL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "3i1doRHD2-ia"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}