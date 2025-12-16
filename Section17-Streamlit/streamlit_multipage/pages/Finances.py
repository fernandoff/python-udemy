import yfinance as yf
import streamlit as st

st.title("Análise Financeira")

ticker_symbol = st.text_input("Digite o símbolo do ativo (ex: AAPL, MSFT, GOOGL):", "AAPL")
if ticker_symbol:
    ticker = yf.Ticker(ticker_symbol)
    hist = ticker.history(period="1y")

    st.subheader(f"Histórico de Preços de {ticker_symbol} - Último Ano")
    st.line_chart(hist['Close'])

    st.subheader(f"Informações de {ticker_symbol}")
    info = ticker.info
    st.write(f"**Nome:** {info.get('longName', 'N/A')}")
    st.write(f"**Setor:** {info.get('sector', 'N/A')}")
    st.write(f"**Indústria:** {info.get('industry', 'N/A')}")
    st.write(f"**Website:** {info.get('website', 'N/A')}")
    st.write(f"**Descrição:** {info.get('longBusinessSummary', 'N/A')}")
    st.subheader(f"Dividendo de {ticker_symbol}")
    st.write(f"**Rendimento de Dividendos:** {info.get('dividendYield', 'N/A')}")
    st.write(f"**Último Dividendo:** {info.get('lastDividendValue', 'N/A')}")
    st.write(f"**Data do Último Dividendo:** {info.get('lastDividendDate', 'N/A')}")
    st.subheader(f"Análise Técnica de {ticker_symbol}")
    st.write(f"**Média Móvel de 50 dias:** {hist['Close'].rolling(window=50).mean().iloc[-1]:.2f}")
    st.write(f"**Média Móvel de 200 dias:** {hist['Close'].rolling(window=200).mean().iloc[-1]:.2f}")
    st.write(f"**Volatilidade (Desvio Padrão):** {hist['Close'].pct_change().std() * (252 ** 0.5):.2%}")
else:
    st.write("Por favor, insira um símbolo de ativo válido.")




